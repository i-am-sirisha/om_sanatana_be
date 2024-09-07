from rest_framework import generics,viewsets
from rest_framework.response import Response
from ..models import book
from ..serializers import BookSerializer,BookSerializer1
from ..utils import save_image_to_folder
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from ..pagination import CustomPagination 




class Booksviewsets(viewsets.GenericViewSet):
    quaryset=book.objects.all()
    serializer_class=BookSerializer1
    paginator = CustomPagination()


class BookPostCall(generics.GenericAPIView):
    serializer_class = BookSerializer

    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        pdf_location = request.data.get('pdf_location')
        # print(pdf_location, "vfvfv")
        # Make a mutable copy of request.data
        mutable_data = request.data.copy()
        mutable_data['pdf_location'] = "null"
        # Instantiate the serializer with the mutable copy
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if pdf_location and pdf_location != "null":
            saved_location = save_image_to_folder(pdf_location, serializer.instance._id,serializer.instance.name)
            if saved_location:
                serializer.instance.pdf_location = saved_location
                print(serializer.instance.pdf_location, "referg")
                serializer.instance.save()
        return Response({
            "message": "success",
            "result": serializer.data
        })


class BookUpdateCall(generics.GenericAPIView):
    serializer_class = BookSerializer
    def put(self, request, _id):
        # Retrieve the instance
        instance = get_object_or_404(book, _id=_id)
        # Retrieve image_location from request data
        pdf_location = request.data.get('pdf_location')
        # print(pdf_location, "vfvfv")
        # Make a mutable copy of request.data and set image_location to "null"
        mutable_data = request.data.copy()
        mutable_data['pdf_location'] = "null"
        # Instantiate the serializer with the mutable copy of data
        serializer = self.get_serializer(instance, data=mutable_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # If image_location is provided and not "null", save the image
        if pdf_location and pdf_location != "null":
            saved_location = save_image_to_folder(pdf_location, serializer.instance._id, serializer.instance.category_id.name)
            if saved_location:
                serializer.instance.pdf_location = saved_location
                print(serializer.instance.image_location, "referg")
                serializer.instance.save()
        # Return the response with the updated data
        return Response(BookSerializer(serializer.instance).data, status=status.HTTP_200_OK)
    

# class book_GetItemByfield_InputView(APIView):
#     serializer_class = BookSerializer1

#     def get(self, request, input_value, field_name):
#         try:
#             # Get all field names of the NewsCategory model
#             field_names = [field.name for field in book._meta.get_fields()]
#             print(field_names, "Available field names")

#             # Check if the field_name provided is valid
#             if field_name in field_names:
#                 filter_kwargs = {field_name: input_value}
#                 print(filter_kwargs, "Filter arguments")

#                 # Filter the queryset based on the dynamic field name and value
#                 queryset = book.objects.filter(**filter_kwargs)
#                 print(queryset,"ghtyguyguiyg")

#                 # # Process the data based on the 'status' field
#                 # if field_name != 'status':
#                 #     queryset = queryset.filter(status=EntityStatus.SUCCESS.value)

#                 # Apply pagination to the filtered queryset
#                 paginator = CustomPagination()
#                 paginated_queryset = paginator.paginate_queryset(queryset, request)
                
#                 # Serialize the paginated queryset
#                 serialized_data = BookSerializer1(paginated_queryset, many=True)
                
#                 return paginator.get_paginated_response(serialized_data.data)

#             else:
#                 return Response({
#                     'message': 'Invalid field name',
#                     'status': 400
#                 }, status=status.HTTP_400_BAD_REQUEST)

#         except book.DoesNotExist:
#             return Response({
#                 'message': 'Object not found',
#                 'status': 404
#             }, status=status.HTTP_404_NOT_FOUND)



class book_GetItemByfield_InputView(APIView):
    serializer_class = BookSerializer1
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = book.objects.all()

        category_id = request.query_params.get('category_id')
        news_sub_category_id = request.query_params.get('news_sub_category_id')
        _id = request.query_params.get('_id')
        name = request.query_params.get('name')
        

        # Filter by category_id if provided
        if _id:
            queryset = queryset.filter(_id=_id)

        if name:
            queryset = queryset.filter(name=name)

        # Filter by category_id if provided
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        # Filter by news_sub_category_id if provided
        if news_sub_category_id:
            queryset = queryset.filter(news_sub_category_id=news_sub_category_id)


        # Pagination
        paginator = CustomPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = BookSerializer1(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

# class BookPostCall(generics.GenericAPIView):
#     serializer_class = BookSerializer

#     # permission_classes = [permissions.IsAuthenticated]
#     def post(self, request, *args, **kwargs):
#         pdf_location = request.FILES.get('pdf_location')
#         mutable_data = request.data.copy()
#         mutable_data['pdf_location'] = None  # This will be set after saving the file
#         serializer = self.get_serializer(data=mutable_data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         if pdf_location:
#             saved_location = save_image_to_folder(pdf_location, serializer.instance._id, serializer.instance.name)
#             if saved_location:
#                 serializer.instance.pdf_location = saved_location
#                 serializer.instance.save()
        
#         return Response({
#             "message": "success",
#             "result": serializer.data
#         })