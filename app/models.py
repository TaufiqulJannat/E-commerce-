from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator


STATE_CHOICE = (
('Dhaka','Dhaka'),
('Chottogram', 'Chottogram'),
('Barisal', 'Barisal'),
('Maymanshing', 'Maymanshing'),
('Rajshahi','Rajshahi'),
('Khulna', 'Khulna'),
('Rangpur', 'Rangpur'),
('Chylet', 'chylet'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField (max_length=200)
    locality = models.CharField (max_length=200)
    city = models.CharField (max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField (choices=STATE_CHOICE, max_length=500)


def _str_(self):
    return str(self.id)


CATEGORY_CHOICE = (
('M','Mobile'),
('L', 'Laptop'),
('TW', 'Top Wear'),
('BW', 'Bottom Wear'),
)   


class Product(models.Model):
    title = models.CharField (max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField (max_length=200)
    category = models.CharField (choices=CATEGORY_CHOICE, max_length=10)
    product_image = models.ImageField(upload_to='productimg')


def _str_(self):
    return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



def _str_(self):
    return str(self.id)

STATUS_CHOICE = (
('Accepted','Accepted'),
('Packed', 'Packed'),
('On The Way', 'On The Way'),
('Delivered', 'Delivered'),
('Cancel', 'Cancel'),
)   
   



class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,
    choices = STATUS_CHOICE, default='pending')    