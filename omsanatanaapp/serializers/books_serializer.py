from rest_framework import serializers
from ..models import book
from ..utils import image_path_to_binary

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

# class BookSerializer1(serializers.ModelSerializer):
#     pdf_location= serializers.SerializerMethodField()
#     def get_pdf_location(self, instance):
#         filename = instance.pdf_location  # Use the correct attribute name
#         if filename:
#             format = image_path_to_binary(filename)
#             return format
#         return []
#     class Meta:
#         model = book
#         fields = "__all__"


from ..utils import extract_pdf_content
import os
from django.conf import settings

class BookSerializer1(serializers.ModelSerializer):
    pdf_content = serializers.SerializerMethodField()

    def get_pdf_content(self, instance):
        if instance.pdf_location:
            file_path = os.path.join(settings.FILE_URL, instance.pdf_location)
            content = extract_pdf_content(file_path)
            return content
        return {"text": "", "images": []}

    class Meta:
        model = book
        fields = "__all__"

# class BookSerializer1(serializers.ModelSerializer):
#     pdf_location = serializers.SerializerMethodField()

#     def get_pdf_location(self, instance):
#         filename = instance.pdf_location
#         if filename:
#             hex_encoded_data = image_path_to_binary(filename)
#             return hex_encoded_data
#         return ""

#     class Meta:
#         model = book
#         fields = '__all__'