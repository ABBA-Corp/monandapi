from django.db import models
from django.contrib.auth.models import User as Customer

class Category(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    icon = models.ImageField(null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_uz
    

class Product(models.Model):
    name_uz = models.CharField(max_length=200, null=True, blank=True)
    name_ru = models.CharField(max_length=200, null=True, blank=True)
    name_en = models.CharField(max_length=200, null=True, blank=True)
    description_uz = models.TextField(max_length=2000, null=True, blank=True)
    description_ru = models.TextField(max_length=2000, null=True, blank=True)
    description_en = models.TextField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_code = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    price = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    top = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name_uz


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    summa = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.customer.name} {self.date}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class CardObject(models.Model):
    cardid = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id = models.IntegerField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default=0)
    
    def clear(customer_id):
        objects = CardObject.objects.filter(customer_id=customer_id).all()
        for object in objects:
            object.delete()


class Like(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
