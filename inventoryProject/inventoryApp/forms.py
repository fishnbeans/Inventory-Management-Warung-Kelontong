from django import forms
from .models import Produk
from .models import Suplier
from .models import Pembelian
from .models import Penjualan

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'
        labels = {
            'produk_id' : 'ID Produk',
            'nama_produk': 'Nama Produk',
            'sku': 'SKU',
            'kategori': 'Kategori',
            'harga_produk': 'Harga Produk',
            'stok': 'Stok',
            'tanggal_masuk': 'Tanggal Masuk',
        }
        widgets = {
            'produk_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'kategori': forms.TextInput(attrs={'class': 'form-control'}),
            'harga_produk': forms.NumberInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'tanggal_masuk': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

class SuplierForm(forms.ModelForm):
    class Meta:
        model = Suplier
        fields = '__all__'
        labels = {
            'suplier_id' : 'ID Suplier',
            'nama_suplier': 'Nama Suplier',
            'alamat': 'Alamat',
            'kontak': 'Kontak',
        }
        widgets = {
            'suplier_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama_suplier': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'kontak': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PembelianForm(forms.ModelForm):
    class Meta:
        model = Pembelian
        fields = '__all__'
        labels = {
            'pembelian_id' : 'ID Pembelian',
            'Produk_id': 'Produk',
            'Suplier_id': 'Suplier',
            'jumlah': 'Jumlah',
            'harga_pembelian': 'Harga Pembelian',
            'tanggal_pembelian': 'Tanggal Pembelian',
        }
        widgets = {
            'pembelian_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'Produk_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'Suplier_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}),
            'harga_pembelian': forms.NumberInput(attrs={'class': 'form-control'}),
            'tanggal_pembelian': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

class PenjualanForm(forms.ModelForm):
    class Meta:
        model = Penjualan
        fields = '__all__'
        labels = {
            'penjualan_id' : 'ID Penjualan',
            'Produk_id': 'Produk',
            'jumlah': 'Jumlah',
            'harga_penjualan': 'Harga Penjualan',
            'tanggal_penjualan': 'Tanggal Penjualan',
        }
        widgets = {
            'penjualan_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'Produk_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}),
            'harga_penjualan': forms.NumberInput(attrs={'class': 'form-control'}),
            'tanggal_penjualan': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
        