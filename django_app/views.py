from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_app.serializers import *
from django_app.models import *

from .forms import *
from .models import *


def is_admin(user) :
    return user.is_superuser or user.is_staff


@login_required ( login_url='SignIn' )
def index(request) :
    return render ( request, 'index.html' )


def SignInPage(request) :
    return render ( request, 'SignIn.html' )


@login_required ( login_url='SignIn' )
def categories_with_id(request, category_id) :
    categories = Category.objects.filter ( category_id=category_id )
    return render ( request, 'categories.html', {'categories' : categories} )


@login_required ( login_url='SignIn' )
def products_by_category(request, category_id) :
    products = Product.objects.filter ( category_id=category_id )
    categories = Category.objects.all ()
    return render ( request, 'products.html', {'products' : products, 'categories' : categories} )


@login_required ( login_url='SignIn' )
@user_passes_test ( is_admin, login_url='home' )
def add_news(request) :
    if request.method == 'POST' :
        form = NewsForm ( request.POST, request.FILES )
        if form.is_valid () :
            news = News.objects.create ( **form.cleaned_data )
            return redirect ( 'home' )
    else :
        form = NewsForm ()
    return render ( request, 'add_news.html', {'form' : form} )


@login_required ( login_url='SignIn' )
@user_passes_test ( is_admin, login_url='home' )
def add_category(request) :
    if request.method == 'POST' :
        form = CategoryForm ( request.POST, request.FILES )
        if form.is_valid () :
            category = Category.objects.create ( **form.cleaned_data )
            return redirect ( 'home' )
    else :
        form = CategoryForm ()
    return render ( request, 'add_category.html', {'form' : form} )


@login_required ( login_url='SignIn' )
@user_passes_test ( is_admin, login_url='home' )
def add_product(request) :
    if request.method == 'POST' :
        form = ProductForm ( request.POST, request.FILES )
        if form.is_valid () :
            product = Product.objects.create ( **form.cleaned_data )
            return redirect ( 'home' )
    else :
        form = ProductForm ()
    return render ( request, 'add_product.html', {'form' : form} )


@login_required ( login_url='SignIn' )
@user_passes_test ( is_admin, login_url='home' )
def add_supplier(request) :
    if request.method == 'POST' :
        form = SupplierForm ( request.POST, request.FILES )
        if form.is_valid () :
            supplier = Supplier.objects.create ( **form.cleaned_data )
            return redirect ( 'home' )
    else :
        form = SupplierForm ()
    return render ( request, 'add_supplier.html', {'form' : form} )


class AdminRequiredMixin ( UserPassesTestMixin ) :
    def test_func(self) :
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self) :
        messages.error ( self.request, 'You do not have permission to perform this action.' )
        return redirect ( 'home' )


class HomeNews ( LoginRequiredMixin, ListView ) :
    login_url = 'SignIn'
    model = News
    template_name = 'news.html'
    context_object_name = 'news'


class NewsUpdate ( LoginRequiredMixin, AdminRequiredMixin, UpdateView ) :
    login_url = 'SignIn'
    model = News
    form_class = NewsForm
    template_name = 'update_news.html'
    success_url = reverse_lazy ( 'news' )
    pk_url_kwargs = 'pk'

    def form_valid(self, form) :
        return super ().form_valid ( form )


class NewsDelete ( LoginRequiredMixin, AdminRequiredMixin, DeleteView ) :
    login_url = 'SignIn'
    model = News
    pk_url_kwargs = 'pk'
    success_url = reverse_lazy ( 'news' )

    def delete(self, request, *args, **kwargs) :
        self.object = self.get_object ()
        self.object.delete ()
        return redirect ( self.success_url )


class HomeCategories ( LoginRequiredMixin, ListView ) :
    login_url = 'SignIn'
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'


class CategoryUpdate ( LoginRequiredMixin, AdminRequiredMixin, UpdateView ) :
    login_url = 'SignIn'
    model = Category
    form_class = CategoryForm
    template_name = 'update_category.html'
    success_url = reverse_lazy ( 'categories' )
    pk_url_kwargs = 'pk'

    def form_valid(self, form) :
        return super ().form_valid ( form )


class CategoryDelete ( LoginRequiredMixin, AdminRequiredMixin, DeleteView ) :
    login_url = 'SignIn'
    model = Category
    pk_url_kwargs = 'pk'
    success_url = reverse_lazy ( 'categories' )

    def delete(self, request, *args, **kwargs) :
        self.object = self.get_object ()
        self.object.delete ()
        return redirect ( self.success_url )


class HomeProducts ( LoginRequiredMixin, ListView ) :
    login_url = 'SignIn'
    model = Product
    categories = Category.objects.all ()
    template_name = 'products.html'
    context_object_name = 'products'
    extra_context = {
        'categories' : categories
    }


class ProductUpdate ( LoginRequiredMixin, AdminRequiredMixin, UpdateView ) :
    login_url = 'SignIn'
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy ( 'products' )
    pk_url_kwargs = 'pk'

    def form_valid(self, form) :
        return super ().form_valid ( form )


class ProductDelete ( LoginRequiredMixin, AdminRequiredMixin, DeleteView ) :
    login_url = 'SignIn'
    model = Product
    pk_url_kwargs = 'pk'
    success_url = reverse_lazy ( 'products' )

    def delete(self, request, *args, **kwargs) :
        self.object = self.get_object ()
        self.object.delete ()
        return redirect ( self.success_url )


class HomeSuppliers ( LoginRequiredMixin, ListView ) :
    login_url = 'SignIn'
    model = Supplier
    template_name = 'suppliers.html'
    context_object_name = 'suppliers'


class SupplierUpdate ( LoginRequiredMixin, AdminRequiredMixin, UpdateView ) :
    login_url = 'SignIn'
    model = Supplier
    form_class = SupplierForm
    template_name = 'update_supplier.html'
    success_url = reverse_lazy ( 'suppliers' )
    pk_url_kwargs = 'pk'

    def form_valid(self, form) :
        return super ().form_valid ( form )


class SupplierDelete ( LoginRequiredMixin, AdminRequiredMixin, DeleteView ) :
    login_url = 'SignIn'
    model = Supplier
    pk_url_kwargs = 'pk'
    success_url = reverse_lazy ( 'suppliers' )

    def delete(self, request, *args, **kwargs) :
        self.object = self.get_object ()
        self.object.delete ()
        return redirect ( self.success_url )


def SignIn(request) :
    if request.user.is_authenticated :
        return redirect ( 'home' )

    if request.method == 'POST' :
        username = request.POST.get ( 'username' )
        password = request.POST.get ( 'password' )

        user = authenticate ( request, username=username, password=password )

        if user is not None :
            login ( request, user )
            messages.success ( request, 'Successfully logged in!' )
            next_url = 'home'
            return redirect ( next_url )
        else :
            messages.error ( request, 'Invalid username or password' )

    return render ( request, 'SignIn.html' )


def Logout(request) :
    logout ( request )
    messages.success ( request, 'Successfully logged out!' )
    return redirect ( 'SignIn' )


@login_required ( login_url='SignIn' )
def cart_view(request) :
    cart, _ = Cart.objects.get_or_create ( user=request.user )
    return render ( request, 'Cart.html', {'cart' : cart} )


@login_required ( login_url='SignIn' )
def add_to_cart(request, product_id) :
    if request.method != 'POST' :
        return redirect ( 'products' )

    product = get_object_or_404 ( Product, product_id=product_id )

    if product.quantity <= 0 :
        messages.error ( request, f"{product.product_name} is out of stock!" )
        return redirect ( 'products' )

    cart, _ = Cart.objects.get_or_create ( user=request.user )

    cart_item, created = CartItem.objects.get_or_create (
        cart=cart,
        product=product,
        defaults={'quantity' : 1}
    )

    if not created :
        if cart_item.quantity < product.quantity :
            cart_item.quantity += 1
            cart_item.save ()
            messages.success ( request, f"{product.product_name} quantity increased in cart!" )
        else :
            messages.warning ( request,
                               f"Cannot add more {product.product_name}. Only {product.quantity} available in stock." )
    else :
        messages.success ( request, f"{product.product_name} has been added to the cart!" )

    return redirect ( 'products' )


@login_required ( login_url='SignIn' )
def remove_from_cart(request, item_id) :
    item = get_object_or_404 ( CartItem, cart_item_id=item_id, cart__user=request.user )
    product_name = item.product.product_name
    item.delete ()
    messages.success ( request, f"{product_name} has been removed from the cart" )
    return redirect ( 'cart' )


@login_required ( login_url='SignIn' )
def update_cart_quantity(request, cart_item_id) :
    if request.method != 'POST' :
        return redirect ( 'cart' )

    cart_item = get_object_or_404 ( CartItem, cart_item_id=cart_item_id, cart__user=request.user )
    action = request.POST.get ( 'action' )

    if action == 'increase' :
        if cart_item.quantity < cart_item.product.quantity :
            cart_item.quantity += 1
            cart_item.save ()
            messages.success ( request, f"{cart_item.product.product_name} quantity increased!" )
        else :
            messages.warning ( request,
                               f"Cannot add more {cart_item.product.product_name}. Only {cart_item.product.quantity} available in stock." )

    elif action == 'decrease' :
        if cart_item.quantity > 1 :
            cart_item.quantity -= 1
            cart_item.save ()
            messages.success ( request, f"{cart_item.product.product_name} quantity decreased!" )
        else :
            product_name = cart_item.product.product_name
            cart_item.delete ()
            messages.info ( request, f"{product_name} has been removed from the cart" )

    return redirect ( 'cart' )


@login_required ( login_url='SignIn' )
def clear_cart(request) :
    if request.method == 'POST' :
        cart = get_object_or_404 ( Cart, user=request.user )
        items_count = cart.items.count ()
        cart.items.all ().delete ()
        messages.success ( request, f"{items_count} item(s) removed from cart" )
    return redirect ( 'cart' )


@swagger_auto_schema (
    method='get',
    responses={200 : CategorySerializer ( many=True )}
)
@swagger_auto_schema (
    method='post',
    request_body=CategorySerializer,
    responses={201 : CategorySerializer ()}
)
@api_view ( ['GET', 'POST'] )
def category_list_create(request) :
    if request.method == 'GET' :
        categories = Category.objects.all ()
        serializer = CategorySerializer ( categories, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    elif request.method == 'POST' :
        serializer = CategorySerializer ( data=request.data )
        if serializer.is_valid ( raise_exception=True ) :
            serializer.save ()
            return Response ( data=serializer.data, status=status.HTTP_201_CREATED )
        return Response ( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    return None


@swagger_auto_schema (
    method='get',
    responses={200 : ProductSerializer ( many=True )}
)
@swagger_auto_schema (
    method='post',
    request_body=ProductSerializer,
    responses={201 : ProductSerializer ()}
)
@api_view ( ['GET', 'POST'] )
def product_list_create(request) :
    if request.method == 'GET' :
        products = Product.objects.all ()
        serializer = ProductSerializer ( products, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    elif request.method == 'POST' :
        serializer = ProductSerializer ( data=request.data )
        if serializer.is_valid ( raise_exception=True ) :
            serializer.save ()
            return Response ( data=serializer.data, status=status.HTTP_201_CREATED )
        return Response ( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    return None


@swagger_auto_schema (
    method='get',
    responses={200 : SupplierSerializer ( many=True )}
)
@swagger_auto_schema (
    method='post',
    request_body=SupplierSerializer,
    responses={201 : SupplierSerializer ()}
)
@api_view ( ['GET', 'POST'] )
def supplier_list_create(request) :
    if request.method == 'GET' :
        suppliers = Supplier.objects.all ()
        serializer = SupplierSerializer ( suppliers, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    elif request.method == 'POST' :
        serializer = SupplierSerializer ( data=request.data )
        if serializer.is_valid ( raise_exception=True ) :
            serializer.save ()
            return Response ( data=serializer.data, status=status.HTTP_201_CREATED )
        return Response ( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    return None


@swagger_auto_schema (
    method='get',
    responses={200 : NewsSerializer ( many=True )}
)
@swagger_auto_schema (
    method='post',
    request_body=NewsSerializer,
    responses={201 : NewsSerializer ()}
)
@api_view ( ['GET', 'POST'] )
def news_list_create(request) :
    if request.method == 'GET' :
        news = News.objects.all ()
        serializer = NewsSerializer ( news, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    elif request.method == 'POST' :
        serializer = NewsSerializer ( data=request.data )
        if serializer.is_valid ( raise_exception=True ) :
            serializer.save ()
            return Response ( data=serializer.data, status=status.HTTP_201_CREATED )
        return Response ( serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    return None