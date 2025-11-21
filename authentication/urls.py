from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.sign_in),
    path('register/', views.register),
    path('logout/', views.terminate_session),
]