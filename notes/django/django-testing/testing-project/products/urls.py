from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('product-list/', views.product_list, name='product_list'),
]
