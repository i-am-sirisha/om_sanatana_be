# from rest_framework import serializers
# from ..models import book
# from ..utils import image_path_to_binary

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = book
#         fields = '__all__'

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


from rest_framework import serializers
from ..models import Book, PDF
from rest_framework import serializers
from ..models import Book, PDF
import os,base64

# class PDFSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PDF
#         fields = ['_id', 'name', 'file_path']

# class BookSerializer(serializers.ModelSerializer):
#     pdf_files = PDFSerializer(many=True, read_only=True)

#     class Meta:
#         model = Book
#         fields = '__all__'

class BookSerializer1(serializers.ModelSerializer):
    pdf_files = serializers.SerializerMethodField()

    def get_pdf_files(self, instance):
        return PDFSerializer(instance.pdf_files.all(), many=True).data

    class Meta:
        model = Book
        fields = "__all__"


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = ['_id', 'name', 'file_path']

class PDFSerializer1(serializers.ModelSerializer):
    file_path = serializers.SerializerMethodField()

    class Meta:
        model = PDF
        fields = ['name', 'file_path']

    def get_file_path(self, instance):
        try:
            file_path = instance.file_path
            if os.path.exists(file_path):
                with open(file_path, "rb") as pdf_file:
                    pdf_data = pdf_file.read()
                    # Encode the PDF data as Base64
                    return base64.b64encode(pdf_data).decode('utf-8')
            return None
        except Exception as e:
            return str(e)

class BookSerializer(serializers.ModelSerializer):
    pdf_files = PDFSerializer(many=True, read_only=True)  # Include related PDFs

    class Meta:
        model = Book
        fields = ['_id', 'name', 'category_id', 'news_sub_category_id', 'pdf_files']

class BookSerializer2(serializers.ModelSerializer):
    pdf_files = PDFSerializer1(many=True, read_only=True)  # Include related PDFs

    class Meta:
        model = Book
        fields = ['_id', 'name', 'category_id', 'news_sub_category_id', 'pdf_files']
