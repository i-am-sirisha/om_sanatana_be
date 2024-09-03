from rest_framework import generics,viewsets
from rest_framework.response import Response
# from ..models import book
from ..serializers import BookSerializer,BookSerializer1
from ..utils import save_image_to_folder
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from ..pagination import CustomPagination 


from rest_framework import generics, viewsets
from rest_framework.response import Response
from ..models import Book, PDF
from ..serializers import BookSerializer, BookSerializer1
from ..utils import save_image_to_folder
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from ..pagination import CustomPagination



from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ..models import Book, PDF
from ..serializers import BookSerializer, BookSerializer1,BookSerializer2
from ..utils import save_image_to_folder,save_base64_to_folder

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer2

class BookPostCall(generics.GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        pdf_files = request.data.get('pdf_files', [])
        mutable_data = request.data.copy()
        mutable_data['pdf_files'] = []  # Initialize with an empty list
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        for pdf_data in pdf_files:
            pdf_base64 = pdf_data.get('base64')  # Assuming base64 is the key in PDF object
            file_name = pdf_data.get('name', 'default.pdf')  # Assuming name is the key
            if pdf_base64:
                saved_location = save_base64_to_folder(pdf_base64, instance._id, file_name)
                pdf = PDF.objects.create(name=file_name, file_path=saved_location)
                instance.pdf_files.add(pdf)

        return Response({
            "message": "success",
            "result": BookSerializer(instance).data
        })
    

class BookUpdateCall(generics.GenericAPIView):
    serializer_class = BookSerializer

    def put(self, request, _id):
        # Retrieve the book instance
        instance = get_object_or_404(Book, _id=_id)
        pdf_files = request.data.get('pdf_files', [])

        # Prepare the mutable data for the serializer
        mutable_data = request.data.copy()
        mutable_data['pdf_files'] = []  # Initialize with an empty list to avoid issues
        serializer = self.get_serializer(instance, data=mutable_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Clear existing PDF files related to this book
        instance.pdf_files.all().delete()

        # Handle new PDFs
        for pdf_data in pdf_files:
            pdf_base64 = pdf_data.get('base64')  # Assuming base64 is the key in PDF object
            file_name = pdf_data.get('name', 'default.pdf')  # Assuming name is the key
            if pdf_base64:
                saved_location = save_base64_to_folder(pdf_base64, instance._id, file_name)
                pdf = PDF.objects.create(name=file_name, file_path=saved_location)
                instance.pdf_files.add(pdf)

        return Response({
            "message": "success",
            "result": BookSerializer(instance).data
        }, status=status.HTTP_200_OK)

