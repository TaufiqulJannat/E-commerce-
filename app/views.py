from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html',
        {'topwears':topwears,'bottomwears':bottomwears,
        'mobiles':mobiles,'laptops':laptops})

#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',
        {'product' :product})




def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def login(request):
 return render(request, 'app/login.html')


def checkout(request):
 return render(request, 'app/checkout.html')



#For registration
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
        {'form':form})


    def post (self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'app/customerregistration.html',
        {'form':form})     

    





#Start For Mobile
def mobile(request, data = None):
 if data == None:
     mobiles = Product.objects.filter(category='M')
 elif data == 'VIVO' or data == 'IPhone' or data == 'OPPO' :
     mobiles = Product.objects.filter(category='M').filter(brand=data)

 elif data == 'below' :
     mobiles = Product.objects.filter(category='M').filter(discount_price__lt=10000)

 elif data == 'above' :
     mobiles = Product.objects.filter(category='M').filter(discount_price__gt=10000)

 return render(request, 'app/mobile.html', {'mobiles' : mobiles})

#Finish For Mobile


#Start For Laptop
def laptop(request, data = None):
 if data == None:
     laptops = Product.objects.filter(category='L')
 elif data == 'HP' or data == 'APPLE' or data == 'DELL' :
     laptops = Product.objects.filter(category='L').filter(brand=data)

 elif data == 'below' :
     laptops = Product.objects.filter(category='L').filter(discount_price__lt=10000)

 elif data == 'above' :
     laptops = Product.objects.filter(category='L').filter(discount_price__gt=10000)

 return render(request, 'app/laptop.html', {'laptops' : laptops})

#Finish For Laptop


#Start For topwear
def topwear(request, data = None):
 if data == None:
     topwears = Product.objects.filter(category='TW')
 elif data == 'MENSWORLD' or data == 'EASY' or data == 'RICHMAN' :
     topwears = Product.objects.filter(category='TW').filter(brand=data)

 elif data == 'below' :
     topwears = Product.objects.filter(category='TW').filter(discount_price__lt=10000)

 elif data == 'above' :
     topwears = Product.objects.filter(category='TW').filter(discount_price__gt=10000)

 return render(request, 'app/topwear.html', {'topwears' : topwears})

#Finish For topwear


#Start For Bottomwear
def bottomwear(request, data = None):
 if data == None:
     bottomwears = Product.objects.filter(category='BW')
 elif data == 'EASY' or data == 'RICHMAN' or data == 'CATSEYE' :
     bottomwears = Product.objects.filter(category='BW').filter(brand=data)

 elif data == 'below' :
     bottomwears = Product.objects.filter(category='BW').filter(discount_price__lt=10000)

 elif data == 'above' :
     bottomwears = Product.objects.filter(category='BW').filter(discount_price__gt=10000)

 return render(request, 'app/bottomwear.html', {'bottomwears' : bottomwears})

#Finish For Bottomwear

