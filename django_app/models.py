from django.db import models
from django.contrib.auth.models import User


class Category ( models.Model ) :
    category_id = models.AutoField ( primary_key=True )
    category_name = models.CharField ( max_length=100 )
    description = models.TextField ( default='Default Description' )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', default='images/category.png' )

    def __str__(self) :
        return self.category_name

    class Meta :
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product ( models.Model ) :
    product_id = models.AutoField ( primary_key=True )
    product_name = models.CharField ( max_length=50 )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE )
    unit_price = models.IntegerField ()
    description = models.TextField ( blank=True, null=True )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True, default='images/product.png' )

    def __str__(self) :
        return self.product_name

    class Meta :
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-product_name']


class Supplier ( models.Model ) :
    supplier_id = models.AutoField ( primary_key=True )
    company_name = models.CharField ( max_length=50 )
    contact_name = models.CharField ( max_length=50 )
    contact_title = models.CharField ( max_length=50 )
    address = models.CharField ( max_length=50 )
    city = models.CharField ( max_length=50 )
    region = models.CharField ( max_length=50, blank=True, null=True )
    image = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True, default='images/supplier.png' )

    class Meta :
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


class News ( models.Model ) :
    title = models.CharField ( max_length=100, verbose_name='Title' )
    content = models.TextField ( verbose_name='Content' )
    created_at = models.DateTimeField ( auto_now_add=True, verbose_name='Add_date' )
    updated_at = models.DateTimeField ( auto_now=True )
    photo = models.ImageField ( upload_to='photo/%Y/%m/%d', default='images/news.jpg' )
    bool = models.BooleanField ( default=False, verbose_name='Bool' )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE, default=1 )

    def __str__(self) :
        return self.title

    class Meta :
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_at']


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def get_total_price(self):
        return sum(item.product.unit_price for item in self.items.all())

    def get_total_items(self):
        return self.items.count()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.product_name}"

    def get_total_price(self):
        return self.product.unit_price

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        unique_together = ['cart', 'product']