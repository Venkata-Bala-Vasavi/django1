from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('deleteproduct/',views.deleteproduct,name='deleteproduct'),
    path('carousel/',views.carousel_view,name='carousel'),
    path('grid/', views.grid_view, name='grid'),
]