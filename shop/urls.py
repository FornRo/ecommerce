from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Index.as_view(), name='home'),
    # path('category/<slug:category_slug>', views.Index.as_view(), name='products_by_category'),

    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='products_by_category'),


    # path('<slug:category_slug>', views.Index.as_view(), name='pro'),
    path('about/', views.About.as_view(), name='about'),
]
