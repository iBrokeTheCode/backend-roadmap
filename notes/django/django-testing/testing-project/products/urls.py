from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('product-list/', views.product_list, name='product-list'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('get-user/', views.get_user, name='get-user'),
]
