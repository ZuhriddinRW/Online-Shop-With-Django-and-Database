from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django_app.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view (
    openapi.Info (
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact ( email="contact@snippets.local" ),
        license=openapi.License ( name="BSD License" ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter ()
router.register ( r'news', NewsModelViewSet, basename='news' )
router.register ( r'categories', CategoryModelViewSet, basename='category' )
router.register ( r'products', ProductModelViewSet, basename='product' )
router.register ( r'suppliers', SupplierModelViewSet, basename='supplier' )
router.register ( r'comments', CommentModelViewSet, basename='comment' )

urlpatterns = [
    path ( 'home/', index, name='home' ),
    path ( '', include ( router.urls ) ),

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

    path ( 'signin/', SignIn, name='SignIn' ),
    path ( 'logout/', Logout, name='logout' ),

    path ( 'cart/', cart_view, name='cart' ),
    path ( 'cart/add/<int:product_id>/', add_to_cart, name='add_to_cart' ),
    path ( 'cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart' ),
    path ( 'cart/update/<int:cart_item_id>/', update_cart_quantity, name='update_cart_quantity' ),
    path ( 'cart/clear/', clear_cart, name='clear_cart' ),

    path ( 'swagger<format>/', schema_view.without_ui ( cache_timeout=0 ), name='schema-json' ),
    path ( 'swagger/', schema_view.with_ui ( 'swagger', cache_timeout=0 ), name='schema-swagger-ui' ),
    path ( 'redoc/', schema_view.with_ui ( 'redoc', cache_timeout=0 ), name='schema-redoc' ),

    path ( 'api-token-auth/', obtain_auth_token )
]