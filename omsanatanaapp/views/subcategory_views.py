from rest_framework import viewsets
from ..models import SubCategory
from ..serializers import SubCategorySerializer
from ..pagination import CustomPagination 
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework.views import APIView
from rest_framework import status





class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = CustomPagination 
    

class GetSubCategoryById_InputView(APIView):
    # serializer_class = NewsSubCategorySerializer

    def get(self, request, _id):
        try:
           
            field_names = [field.name for field in SubCategory._meta.get_fields()]
            print(field_names, "Available field names")
         
            filter_kwargs = {"other_category": _id}
            print(filter_kwargs, "Filter arguments")

           
            queryset = SubCategory.objects.filter(**filter_kwargs)
          
            paginator = CustomPagination()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            
            
            serialized_data = SubCategorySerializer(paginated_queryset, many = True)
            return paginator.get_paginated_response(serialized_data.data)
        
        except SubCategory.DoesNotExist:
            return Response({
                'message': 'Object not found',
                'status': 404
            }, status=status.HTTP_404_NOT_FOUND)





