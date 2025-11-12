from django.contrib import admin
from .models import *


class NewsAdmin ( admin.ModelAdmin ) :
    list_display = ('title', 'created_at', 'updated_at', 'category', 'bool')
    list_display_links = ['title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_editable = ['bool']


class ProductAdmin ( admin.ModelAdmin ) :
    list_display = ('product_name', 'category', 'unit_price', 'image')
    list_display_links = ('product_name', 'category')
    search_fields = ['product_name']


class CategoryAdmin ( admin.ModelAdmin ) :
    list_display = ('category_id', 'category_name', 'description', 'image')
    list_display_links = ('category_id', 'category_name')
    search_fields = ['category_name']


class SupplierAdmin ( admin.ModelAdmin ) :
    list_display = ('supplier_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region',
                    'image')
    list_display_links = ('company_name', 'contact_name')
    search_fields = ['company_name']


admin.site.register ( News, NewsAdmin )
admin.site.register ( Product, ProductAdmin )
admin.site.register ( Category, CategoryAdmin )
admin.site.register ( Supplier, SupplierAdmin )
admin.site.register ( [Cart, CartItem] )