from django_app.models import *
from rest_framework import serializers


class CommentSerializer ( serializers.ModelSerializer ) :
    author_username = serializers.CharField ( source='author.username', read_only=True )

    class Meta :
        model = Comment
        fields = ['comment_id', 'text', 'author_username',
                  'category', 'news', 'created_at', 'is_active']
        read_only_fields = ['comment_id', 'author_username', 'created_at']

    def validate(self, data) :
        category = data.get ( 'category' )
        news = data.get ( 'news' )

        if category and news :
            raise serializers.ValidationError ( "Choose only one of them!" )
        if not category and not news :
            raise serializers.ValidationError ( "Category or News required!" )

        return data


class ProductSerializer ( serializers.ModelSerializer ) :
    class Meta :
        model = Product
        fields = '__all__'


class CategorySerializer ( serializers.ModelSerializer ) :
    comments = CommentSerializer ( many=True, read_only=True )

    class Meta :
        model = Category
        fields = '__all__'


class SupplierSerializer ( serializers.ModelSerializer ) :
    class Meta :
        model = Supplier
        fields = '__all__'


class NewsSerializer ( serializers.ModelSerializer ) :
    comments = CommentSerializer ( many=True, read_only=True )
    category_name = serializers.CharField ( source='category.category_name', read_only=True )

    class Meta :
        model = News
        fields = '__all__'