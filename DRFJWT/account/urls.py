from django.urls import path,include
from .views import *
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('resetpassemail/',SendPasswordResetEmailView.as_view(),name='resetpassemail'),
    path('resetpass/<uid>/<token>/',UserPasswordResetView.as_view(),name='resetpass'),
    
]