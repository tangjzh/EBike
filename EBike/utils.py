import os
import hashlib
from datetime import datetime
from django.conf import settings
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image
from io import BytesIO
from django.http import JsonResponse
from rest_framework import status as rstatus


def md5hash(*args):
    t = ""
    for arg in args:
        t += arg
    return hashlib.md5((t + settings.SECRET_KEY + datetime.now().strftime('%Y%m%d%H%M%S')).encode()).hexdigest()

def save_base64_image(model, image_data, field_name):
    """
    Decodes a base64-encoded image and saves it to a Django model's ImageField or FileField.

    Args:
    model: Django model instance (e.g., instance of MyModel).
    image_data: Base64 encoded string containing the image.
    field_name: String, the name of the model field to save the image to.
    """
    # Assuming the base64 string is in the format 'data:image/png;base64,iVBORw0K...'
    format, imgstr = image_data.split(';base64,')  # splits the string on ';base64,' and returns a list
    ext = format.split('/')[-1]  # splits the first part on '/' and uses the last part (e.g., 'png')

    # Decode the base64 string
    data = base64.b64decode(imgstr)

    # Convert to a Django file-like object
    django_file = ContentFile(data, name='temp.' + ext)  # e.g., 'temp.png'

    # Save the image to the model's field
    getattr(model, field_name).save(django_file.name, django_file, save=True)

def is_base64_image(base64_str):
    """
    Checks if the provided string is a valid Base64 encoded image.

    Args:
    base64_str (str): The Base64 string to check.

    Returns:
    bool: True if the string is a valid Base64 encoded image, False otherwise.
    """
    # Check if this is a Data URI scheme
    if not base64_str.startswith('data:image/'):
        return False

    # Find the start of the Base64 string
    try:
        header, base64_encoded = base64_str.split(';base64,')
    except ValueError:
        return False

    # Try to decode the Base64 string
    try:
        image_data = base64.b64decode(base64_encoded)
    except base64.binascii.Error:
        return False

    # Try to open the image with PIL to check if it's a valid image file
    try:
        image = Image.open(BytesIO(image_data))
        image.verify()  # Verify that it's a valid image
    except (IOError, ValueError):
        return False

    return True

def response(success, data=None, error=None, status=None):
    if success:
        return JsonResponse({"message": "Success", "results": data}, status=status or rstatus.HTTP_200_OK)
    else:
        return JsonResponse({"message": "Fail", "error": error}, status=status or rstatus.HTTP_400_BAD_REQUEST)
