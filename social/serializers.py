from rest_framework import serializers
from .models import Post, Comment, Tag, PostImage, User, Interaction
from .models import Room, Message
from django.core.files.base import ContentFile
import base64
import uuid

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']

    def to_internal_value(self, data):
        # Check if the incoming data for the image is a string (base64)
        image = data.get('image', None)
        if isinstance(image, str) and image.startswith('data:image'):
            # Base64 encoded image
            format, imgstr = image.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name=f"{id}.{ext}")  # create a Django ContentFile
            data = super().to_internal_value({'image': data})
            return data
        else:
            # Default file upload
            return super().to_internal_value(data)

    def create(self, validated_data):
        return PostImage.objects.create(**validated_data)

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    images = PostImageSerializer(many=True, required=False)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at', 'tags', 'location', 'likes_count', 'views_count', 'images', 'comments']
        extra_kwargs = {'user': {'read_only': True}, 'content': {'required': False}, 'title': {'required': False}}

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        images_data = validated_data.pop('images', None)
        post = Post.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            post.tags.add(tag)
        if images_data:
            for image_data in images_data:
                PostImage.objects.create(post=post, **image_data)
        return post

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    post_title = serializers.ReadOnlyField(source='post.title')
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at', 'likes_count', 'parent', 'replies', 'username', 'post_title']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'post', 'type']
        extra_kwargs = {'type': {'required': False}}

    def create(self, validated_data):
        user = self.context['request'].user
        interaction_type = validated_data.get('type')
        post = validated_data.get('post')

        interaction, created = Interaction.objects.update_or_create(
            user=user, post=post, type=interaction_type,
            defaults={'type': interaction_type}
        )
        return interaction
    
class ToggleFollowSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def validate_user_id(self, value):
        if value == self.context['request'].user.id:
            raise serializers.ValidationError("Users cannot follow/unfollow themselves.")
        if not User.objects.filter(pk=value).exists():
            raise serializers.ValidationError("User does not exist.")
        return value

    def save(self, **kwargs):
        user_id = self.validated_data['user_id']
        user = self.context['request'].user
        target_user = User.objects.get(pk=user_id)

        if user.following.filter(pk=user_id).exists():
            user.following.remove(target_user)
            target_user.following.remove(user)
            action = 'unfollowed'
        else:
            user.following.add(target_user)
            target_user.following.add(user)
            action = 'followed'
        
        return target_user, action

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'timestamp']

class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'participants', 'messages']