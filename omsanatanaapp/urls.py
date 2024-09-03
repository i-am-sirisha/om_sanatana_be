

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# from .views import Registerview,LoginApiView,VerifyOtpView,ResendOtp,ForgotOtp,ResetPassword

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('book', BookViewSet, basename='book')
router.register('sub_category', SubCategoryViewSet, basename='sub_category')


urlpatterns = [
    path('', include(router.urls)),
    path('BookUpdateCall/<str:_id>/', BookUpdateCall.as_view(), name='BookUpdateCall'),
    path('BookPostCall/', BookPostCall.as_view(), name='BookPostCall'),
    path('category_get_by_field/<str:field_name>/<str:input_value>/', Category_GetItemByfield_InputView.as_view(), name='get_category_by_field'),
    path('sub_category_by_id/<str:_id>/', GetSubCategoryById_InputView.as_view(), name="sub_category_by_id"),
    # path('book_GetItemByfield_InputView/<str:field_name>/<str:input_value>/', book_GetItemByfield_InputView.as_view()),



  
]