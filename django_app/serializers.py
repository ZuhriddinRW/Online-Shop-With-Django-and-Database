from django_app.models import *
from rest_framework import serializers


class ProductSerializer ( serializers.ModelSerializer ) :
    class Meta :
        model = Product
        fields = '__all__'


class CategorySerializer ( serializers.ModelSerializer ) :
    class Meta :
        model = Category
        fields = '__all__'


class SupplierSerializer ( serializers.ModelSerializer ) :
    class Meta :
        model = Supplier
        fields = '__all__'


class NewsSerializer ( serializers.ModelSerializer ) :
    class Meta :
        model = News
        fields = '__all__'