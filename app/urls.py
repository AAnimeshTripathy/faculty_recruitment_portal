from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('forgot-password/',views.forgotPassword,name="forgot-password"),
]
