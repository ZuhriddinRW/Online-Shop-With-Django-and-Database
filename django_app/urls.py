from django.urls import path
from .views import *

urlpatterns = [
    path ( '', index, name='home' ),

    path ( 'news', HomeNews.as_view (), name='news' ),
    path ( 'add_news/', add_news, name="add_news" ),
    path ( 'news/update/<int:pk>/', NewsUpdate.as_view (), name='update_news' ),
    path ( 'news/delete/<int:pk>/', NewsDelete.as_view (), name='delete_news' ),

    path ( 'categories', HomeCategories.as_view (), name='categories' ),
    path ( 'add_category/', add_category, name="add_category" ),
    path ( 'category/update/<int:pk>/', CategoryUpdate.as_view (), name='update_category' ),
    path ( 'category/delete/<int:pk>/', CategoryDelete.as_view (), name='delete_category' ),

    path ( 'products', HomeProducts.as_view (), name='products' ),
    path ( 'add_product/', add_product, name="add_product" ),
    path ( 'product/update/<int:pk>/', ProductUpdate.as_view (), name='update_product' ),
    path ( 'product/delete/<int:pk>/', ProductDelete.as_view (), name='delete_product' ),

    path ( 'suppliers', HomeSuppliers.as_view (), name='suppliers' ),
    path ( 'add_supplier/', add_supplier, name="add_supplier" ),
    path ( 'supplier/update/<int:pk>/', SupplierUpdate.as_view (), name='update_supplier' ),
    path ( 'supplier/delete/<int:pk>/', SupplierDelete.as_view (), name='delete_supplier' ),

    path ( 'categories/<int:category_id>/', categories_with_id, name='categories_by_id' ),
    path ( 'products/<int:category_id>/', products_by_category, name='products_by_category' ),

    path ( 'signin/', SignIn, name='signin' ),
    path ( 'logout/', Logout, name='logout' ),

    path ( 'cart/', cart_view, name='cart' ),
    path ( 'add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart' ),
    path ( 'remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart' ),
]
