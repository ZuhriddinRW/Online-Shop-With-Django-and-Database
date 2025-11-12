import re
from django import forms
from django.core.exceptions import ValidationError
from django_app.models import Category, Product, Supplier, News

from django import forms
from django.core.exceptions import ValidationError
from .models import *
import re


class NewsForm ( forms.ModelForm ) :
    class Meta :
        model = News
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter article title'
            } ),
            'content' : forms.Textarea ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'rows' : 8,
                'placeholder' : 'Write your article content here...'
            } ),
            'category' : forms.Select ( attrs={
                'class' : 'form-select border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none'
            } ),
            'photo' : forms.FileInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'accept' : 'image/*'
            } ),
            'bool' : forms.CheckboxInput ( attrs={
                'class' : 'form-check-input h-5 w-5 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            } )
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['photo'].required = False
        self.fields['bool'].required = False

    def clean_title(self) :
        title = self.cleaned_data.get ( 'title', '' ).strip ()

        if not title :
            raise ValidationError ( 'Title is required' )

        if re.search ( r'\d', title ) :
            raise ValidationError ( 'Title must not contain digits' )

        if len ( title ) < 5 :
            raise ValidationError ( 'Title must be at least 5 characters long' )

        if len ( title ) > 200 :
            raise ValidationError ( 'Title must be less than 200 characters' )

        return title

    def clean_content(self) :
        content = self.cleaned_data.get ( 'content', '' ).strip ()

        if not content :
            raise ValidationError ( 'Content is required' )

        if len ( content ) < 20 :
            raise ValidationError ( 'Content must be at least 20 characters long' )

        return content


class CategoryForm ( forms.ModelForm ) :
    class Meta :
        model = Category
        fields = '__all__'
        widgets = {
            'category_name' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter category name',
            } ),
            'description' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 6,
                'style' : 'resize: vertical; min-height: 120px;',
                'placeholder' : 'Enter description (e.g., Toys and games for kids)',
            } ),
            'image' : forms.ClearableFileInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
            } ),
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['description'].required = False
        self.fields['image'].required = False

    def clean_category_name(self) :
        category_name = self.cleaned_data.get ( 'category_name', '' ).strip ()

        if not category_name :
            raise ValidationError ( 'Category name is required' )

        if not category_name[0].isupper () :
            raise ValidationError ( 'Category name must start with an uppercase letter' )

        if re.search ( r'\d', category_name ) :
            raise ValidationError ( 'Category name must not contain digits' )

        return category_name


class ProductForm ( forms.ModelForm ) :
    class Meta :
        model = Product
        fields = "__all__"
        widgets = {
            'product_name' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
                'placeholder' : 'Enter product name',
            } ),
            'category' : forms.Select ( attrs={
                'class' : 'form-select rounded-3 border-primary',
            } ),
            'unit_price' : forms.NumberInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'placeholder' : 'Enter unit price',
            } ),
            'description' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 6,
                'style' : 'resize: vertical; min-height: 120px;',
                'placeholder' : 'Enter description (e.g., Database design principles)',
            } ),
            'image' : forms.ClearableFileInput ( attrs={
                'class' : 'form-control rounded-3 border-primary',
            } ),
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['description'].required = False
        self.fields['image'].required = False

    def clean_product_name(self) :
        product_name = self.cleaned_data.get ( 'product_name', '' ).strip ()

        if not product_name :
            raise ValidationError ( 'Product name is required' )

        if not re.match ( r'^[a-zA-Z\s]+$', product_name ) :
            raise ValidationError ( 'Product name must contain only letters and spaces (no digits or punctuation)' )

        return product_name

    def clean_unit_price(self) :
        unit_price = self.cleaned_data.get ( 'unit_price' )

        if unit_price is None :
            raise ValidationError ( 'Unit price is required' )

        if unit_price <= 1 :
            raise ValidationError ( 'Unit price must be greater than $1' )

        if unit_price >= 10000 :
            raise ValidationError ( 'Unit price must be less than $10000' )

        return unit_price


class SupplierForm ( forms.ModelForm ) :
    class Meta :
        model = Supplier
        fields = '__all__'
        widgets = {
            'company_name' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter company name'
            } ),
            'contact_name' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter contact name'
            } ),
            'contact_title' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter contact title'
            } ),
            'address' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter address'
            } ),
            'city' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter city name'
            } ),
            'region' : forms.TextInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'placeholder' : 'Enter region (optional)'
            } ),
            'image' : forms.FileInput ( attrs={
                'class' : 'form-control border-2 border-gray-300 rounded-lg p-2 w-full focus:border-blue-500 focus:outline-none',
                'accept' : 'image/*'
            } )
        }

    def __init__(self, *args, **kwargs) :
        super ().__init__ ( *args, **kwargs )
        self.fields['image'].required = False
        self.fields['region'].required = False

    def clean_company_name(self) :
        company_name = self.cleaned_data.get ( 'company_name', '' ).strip ()

        if not company_name :
            raise ValidationError ( 'Company name is required' )

        if re.search ( r'\d', company_name ) :
            raise ValidationError ( 'Company name must not contain digits' )

        if len ( company_name ) < 2 :
            raise ValidationError ( 'Company name must be at least 2 characters long' )

        return company_name

    def clean_contact_name(self) :
        contact_name = self.cleaned_data.get ( 'contact_name', '' ).strip ()

        if not contact_name :
            raise ValidationError ( 'Contact name is required' )

        if len ( contact_name ) < 2 :
            raise ValidationError ( 'Contact name must be at least 2 characters long' )

        return contact_name

    def clean_contact_title(self) :
        contact_title = self.cleaned_data.get ( 'contact_title', '' ).strip ()

        if not contact_title :
            raise ValidationError ( 'Contact title is required' )

        if len ( contact_title ) < 2 :
            raise ValidationError ( 'Contact title must be at least 2 characters long' )

        return contact_title

    def clean_address(self) :
        address = self.cleaned_data.get ( 'address', '' ).strip ()

        if not address :
            raise ValidationError ( 'Address is required' )

        if len ( address ) < 5 :
            raise ValidationError ( 'Address must be at least 5 characters long' )

        return address

    def clean_city(self) :
        city = self.cleaned_data.get ( 'city', '' ).strip ()

        if not city :
            raise ValidationError ( 'City field is required' )

        if not city[0].isupper () :
            raise ValidationError ( 'City name must start with an uppercase letter' )

        if len ( city ) < 3 or len ( city ) > 50 :
            raise ValidationError ( 'City name must be between 3 and 50 characters long' )

        return city

    def clean_region(self) :
        region = self.cleaned_data.get ( 'region' )

        if not region :
            return None

        region = str ( region ).strip () if region else None

        if not region :
            return None

        if not region[0].isupper () :
            raise ValidationError ( 'Region name must start with an uppercase letter' )

        if len ( region ) < 3 or len ( region ) > 50 :
            raise ValidationError ( 'Region name must be between 3 and 50 characters long' )

        return region