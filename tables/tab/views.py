from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
def product_list(request):
    products = Product.objects.all() 
    return render(request, 'product.html', {'products': products}) 
def addproduct(request):
    products = [
        Product(name="Leather Wallet", description="Handcrafted genuine leather wallet with multiple card slots", price=49.99),
        Product(name="Running Shoes", description="Lightweight and comfortable running shoes for all terrains", price=89.99),
        Product(name="Yoga Mat", description="Eco-friendly, non-slip yoga mat for all fitness levels", price=39.99),
        Product(name="Wooden Dining Table", description="Solid oak wood dining table, seats up to 6 people", price=499.99),
        Product(name="Premium Leather Belt", description="Durable full-grain leather belt with adjustable buckle", price=34.99),
        Product(name="Organic Green Tea", description="100% organic green tea leaves for a refreshing taste", price=19.99),
    ]
    Product.objects.bulk_create(products)
    return HttpResponse("Products added successfully!")
def deleteproduct(request):
    Product.objects.all().delete()  
    return HttpResponse("All products have been deleted.")
def carousel_view(request):
    return render(request,'carousel.html')
def grid_view(request):
    return render(request,'grid.html')