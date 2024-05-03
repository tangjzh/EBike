from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable): 
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段
    author = indexes.CharField(model_attr='user')  # 创建一个author字段,model_attr='author'代表对应数据模型ArticlePost中的author字段，可以删
    # title = indexes.CharField(model_attr='title')  # 创建一个title字段
    # body = indexes.CharField(model_attr='body')

    def get_model(self):
        return Post

    # 针对哪些数据进行查询
    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()