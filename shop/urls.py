from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('<slug:category_slug>', views.Index.as_view(), name='products_by_category'),

    path('about/', views.About.as_view(), name='about'),
]
