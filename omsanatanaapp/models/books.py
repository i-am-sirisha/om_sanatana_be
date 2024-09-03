# import uuid
# from .category import Category
# from .subcategory import SubCategory
# from django.db import models




# class book(models.Model):
#     _id = models.CharField(db_column='_id', primary_key=True, max_length=45, default=uuid.uuid1, unique=True, editable=False)
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=45, related_name='category_id')
#     news_sub_category_id = models.ForeignKey(SubCategory,null=True, on_delete=models.CASCADE,related_name="news_sub_category_id")
#     pdf_location = models.TextField(blank=True, null=True)
#     name = models.CharField(db_column='name', max_length=100, unique=True)
   
   
#     class Meta:
#         db_table = "news"


#     def __str__(self):
#         return f'{self.name}'





from django.db import models
import uuid
from .category import Category
from .subcategory import SubCategory

from django.db import models

class PDF(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file_path = models.TextField()  # This will store the path to the saved PDF

    def __str__(self):
        return self.name
from django.db import models
import uuid

class Book(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45, default=uuid.uuid1, unique=True, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    news_sub_category_id = models.ForeignKey(SubCategory, null=True, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(db_column='name', max_length=100, unique=True)
    pdf_files = models.ManyToManyField(PDF, blank=True)  # Relationship to store multiple PDFs

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.name
