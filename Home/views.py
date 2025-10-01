from django.shortcuts import render
from Products.models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'Home/index.html',{'products':products})