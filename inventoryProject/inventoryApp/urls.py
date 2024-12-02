from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/produk', views.produk_create_view, name='produk_create'),
    path('list/produk', views.produk_list_view, name='produk_list'),
    path('update/<int:produk_id>/', views.produk_update_view, name='produk_update'),
    path('delete/<int:produk_id>/', views.produk_delete_view, name='produk_delete'),
    path('create/suplier', views.suplier_create_view, name='suplier_create'),
    path('list/suplier', views.suplier_list_view, name='suplier_list'),
    path('update/<int:suplier_id>/sup', views.suplier_update_view, name='suplier_update'),
    path('delete/<int:suplier_id>/sup', views.suplier_delete_view, name='suplier_delete'),
    path('create/pembelian', views.pembelian_create_view, name='pembelian_create'),
    path('list/pembelian', views.pembelian_list_view, name='pembelian_list'),
    path('update/<int:pembelian_id>/pbl', views.pembelian_update_view, name='pembelian_update'),
    path('delete/<int:pembelian_id>/pbl', views.pembelian_delete_view, name='pembelian_delete'),
    path('create/penjualan', views.penjualan_create_view, name='penjualan_create'),
    path('list/penjualan', views.penjualan_list_view, name='penjualan_list'),
    path('update/<int:penjualan_id>/pjl', views.penjualan_update_view, name='penjualan_update'),
    path('delete/<int:penjualan_id>/pjl', views.penjualan_delete_view, name='penjualan_delete'),
]