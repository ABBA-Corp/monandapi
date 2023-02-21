from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginOTPView.as_view(), name='token_obtain_pair'),
    path('user/', UserViewSet.as_view(), name='user_view'),
    path('user/<str:pk>', UserDetailViewSet.as_view(), name='user_view'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('verify_phone/', GenerateOptView.as_view(), name='verify_phone'),
    path('update_phone/', UpdatePhoneView.as_view(), name='update_phone'),
    path('confirm_update_phone/', ConfirmUpdatePhoneView.as_view(), name='confirm_update_phone'),
]