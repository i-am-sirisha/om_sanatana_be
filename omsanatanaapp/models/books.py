import uuid
from .category import Category
from .subcategory import SubCategory
from django.db import models




class book(models.Model):
    _id = models.CharField(db_column='_id', primary_key=True, max_length=45, default=uuid.uuid1, unique=True, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=45, related_name='category_id')
    news_sub_category_id = models.ForeignKey(SubCategory,null=True, on_delete=models.CASCADE,related_name="news_sub_category_id")
    pdf_location = models.TextField(blank=True, null=True)
    name = models.CharField(db_column='name', max_length=100, unique=True)
   
   
    class Meta:
        db_table = "news"


    def __str__(self):
        return f'{self.name}'


    