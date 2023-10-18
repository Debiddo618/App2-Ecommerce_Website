from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # get all the data from database
    product_objects = Product.objects.all()

    # get the item name from the search bar
    item_name = request.GET.get("item_name")

    # filter the item 
    if item_name != "" and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    # Paginator code
    # specify the object and how many
    paginator = Paginator(product_objects,4)
    # get the current page
    page = request.GET.get("page")
    # get all the object on the page
    product_objects = paginator.get_page(page)

    return render(request,"shop/index.html",{"product_objects":product_objects})

# Detail View
def detail(request,id):
    product_object = Product.objects.get(id=id)
    return render(request,"shop/detail.html",{"product_object":product_object})

# CheckoutView
def checkout(request):

    if request.method == "POST":
        items = request.POST.get("items","")
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zipcode = request.POST.get("zipcode","")
        total = request.POST.get("total","")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request,"shop/checkout.html")