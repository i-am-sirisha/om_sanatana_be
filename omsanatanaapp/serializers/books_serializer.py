from rest_framework import serializers
from ..models import book
from ..utils import image_path_to_binary
from ..utils import extract_pdf_content

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'





class BookSerializer1(serializers.ModelSerializer):
    pdf_content = serializers.SerializerMethodField()

    def get_pdf_content(self, instance):
        if instance.pdf_location:
            file_path = instance.pdf_location  # Assuming pdf_location contains the file path
            pdf_content = extract_pdf_content(file_path)
            return pdf_content
        return []

    class Meta:
        model = book
        fields = "__all__"
