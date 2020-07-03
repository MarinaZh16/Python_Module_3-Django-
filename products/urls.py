from django.urls import path
from django.views.generic import TemplateView
from products import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='all_products'),
    path('logo/', views.some_crap, name='logo'),
    path('create/', views.ProductCreate.as_view(), name='add_product'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='edit_product'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_by_id'),
    path('purchases/', views.PurchaseListView.as_view(), name='all_purchases'),
    path('return/', views.ReturnListView.as_view(), name='all_returns'),
]

