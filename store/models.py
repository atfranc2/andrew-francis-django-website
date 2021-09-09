from django.db import models
from django.db.models.indexes import Index

# Create your models here.

"""
Note: The id field is added by defaultm, so we don't need to add it explicitly. If we 
want to override this behaviour, we can add a model field where primary_key=True. 
"""


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # A slug gets added in the search URL (it is a search engine optimization technique)
    slug = models.SlugField()
    # Use for monetary fields
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    # auto now will update field when product is updated
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    '''
    Creates a many to many relationship between products and promotions (i.e. a product can have multiple promotions applied to it 
    and a promotion can be applied to multiple products). 

    Note: By default this will create an inverse relationship in the promotions table called product_set. We can override this convention 
    by setting a value for related_name. 
    '''
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    # Choice fields have a set number of options to choose from. Must be fomatted as follows.
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership_type = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    '''
    Name of inner class is important. It can be used to specify metadata about the table (i.e. default ordering, indexes, table name, etc.)
    
    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]
    '''


class Address(models.Model):
    '''
    Adresses tied to customers with a one-to-one relationship (i.e. Each customer has only one address)

    Setting customer as primary key (primary_key = True) will prevent multiple addresses from being entered
    for one customer. This enforces the one-to-one relationship and prevents it from 
    being a one to many relationship. 

    Delete options (on_delete) include: 
        - Cascade: Deletes address when customer is deleted ion customers table
        - Set_Null: Sets address to null when customer is deletes (only used when field is nullable)
        - Set_Default: Sets field to defualt value
        - Protect: Prevents customer from being deleted if an address for that customer exists

    Note: We don't need to specify the address relationship in the customer class as well. Django does this by default. 

    If instead we wanted to implement a one-to-many relationship between customer and address we would create the reference like this: 
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    '''
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10, null=True)


class Order(models.Model):

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
