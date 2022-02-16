from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('gifts/', views.GiftList.as_view(), name='gift_list'),
    path('gifts/<int:pk>',
         views.GiftDetail.as_view(), name='gift_detail'),
    path('informations/', views.InformationList.as_view(), name='information_list'),
    path('informations/<int:pk>', views.InformationDetail.as_view(), name='information_detail'),
]