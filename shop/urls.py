from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),

    path('category/', include([
        path('<slug:category_slug>', views.Index.as_view(), name='products_by_category'),
        path('<slug:category_slug>/<slug:product_slug>', views.ProductView.as_view(), name='product_detail'),
        ])
    ),

    # path('cart/', views.CartView.as_view(), name='cart'),
    path('cart', views.CartDetailView.as_view(), name='cart_detail'),
    # path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/add/<int:product_id>', views.Add_CartView.as_view(), name='add_cart'),

    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.signUpView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/signout/', views.signoutView, name='signout'),
]


