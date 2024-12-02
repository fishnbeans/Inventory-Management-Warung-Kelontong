from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProdukForm
from .forms import SuplierForm
from .forms import PembelianForm
from .forms import PenjualanForm
from .models import Produk
from .models import Suplier
from .models import Pembelian
from .models import Penjualan

def home_view(request):
    return render(request, 'inventoryApp/home.html')

def produk_create_view(request):
    form = ProdukForm()
    if request.method == "POST":
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    return render(request, 'inventoryApp/produk_form.html', {'form': form})

def produk_list_view(request):
    produk = Produk.objects.all()
    return render(request, 'inventoryApp/produk_list.html', {'produk': produk})

def produk_update_view(request, produk_id):
    produk = Produk.objects.get(produk_id=produk_id)
    form = ProdukForm(instance=produk)
    if request.method == "POST":
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    return render(request, 'inventoryApp/produk_form.html', {'form': form})

def produk_delete_view(request, produk_id):
    produk = Produk.objects.get(produk_id=produk_id)
    if request.method == "POST":
        produk.delete()
        return redirect('produk_list')
    return render(request, 'inventoryApp/produk_confirm_delete.html', {'produk': produk})

def suplier_create_view(request):
    form = SuplierForm()
    if request.method == "POST":
        form = SuplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suplier_list')
    return render(request, 'inventoryApp/suplier_form.html', {'form': form})

def suplier_list_view(request):
    suplier = Suplier.objects.all()
    return render(request, 'inventoryApp/suplier_list.html', {'suplier': suplier})

def suplier_update_view(request, suplier_id):
    suplier = Suplier.objects.get(suplier_id=suplier_id)
    form = SuplierForm(instance=suplier)
    if request.method == "POST":
        form = SuplierForm(request.POST, instance=suplier)
        if form.is_valid():
            form.save()
            return redirect('suplier_list')
    return render(request, 'inventoryApp/suplier_form.html', {'form': form})

def suplier_delete_view(request, suplier_id):
    suplier = Suplier.objects.get(suplier_id=suplier_id)
    if request.method == "POST":
        suplier.delete()
        return redirect('suplier_list')
    return render(request, 'inventoryApp/suplier_confirm_delete.html', {'suplier': suplier})

def pembelian_create_view(request):
    form = PembelianForm()
    if request.method == "POST":
        form = PembelianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pembelian_list')
    return render(request, 'inventoryApp/pembelian_form.html', {'form': form})

def pembelian_list_view(request):
    pembelian = Pembelian.objects.all()
    return render(request, 'inventoryApp/pembelian_list.html', {'pembelian': pembelian})

def pembelian_update_view(request, pembelian_id):
    pembelian = Pembelian.objects.get(pembelian_id=pembelian_id)
    form = PembelianForm(instance=pembelian)
    if request.method == "POST":
        form = PembelianForm(request.POST, instance=pembelian)
        if form.is_valid():
            form.save()
            return redirect('pembelian_list')
    return render(request, 'inventoryApp/pembelian_form.html', {'form': form})

def pembelian_delete_view(request, pembelian_id):
    pembelian = Pembelian.objects.get(pembelian_id=pembelian_id)
    if request.method == "POST":
        pembelian.delete()
        return redirect('pembelian_list')
    return render(request, 'inventoryApp/pembelian_confirm_delete.html', {'pembelian': pembelian})

def penjualan_create_view(request):
    form = PenjualanForm()
    if request.method == "POST":
        form = PenjualanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penjualan_list')
    return render(request, 'inventoryApp/penjualan_form.html', {'form': form})

def penjualan_list_view(request):
    penjualan = Penjualan.objects.all()
    return render(request, 'inventoryApp/penjualan_list.html', {'penjualan': penjualan})

def penjualan_update_view(request, penjualan_id):
    penjualan = Penjualan.objects.get(penjualan_id=penjualan_id)
    form = PenjualanForm(instance=penjualan)
    if request.method == "POST":
        form = PenjualanForm(request.POST, instance=penjualan)
        if form.is_valid():
            form.save()
            return redirect('penjualan_list')
    return render(request, 'inventoryApp/penjualan_form.html', {'form': form})

def penjualan_delete_view(request, penjualan_id):
    penjualan = Penjualan.objects.get(penjualan_id=penjualan_id)
    if request.method == "POST":
        penjualan.delete()
        return redirect('penjualan_list')
    return render(request, 'inventoryApp/penjualan_confirm_delete.html', {'penjualan': penjualan})
