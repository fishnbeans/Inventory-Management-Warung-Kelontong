from django.db import models

# Create your models here.

class Produk(models.Model):
    produk_id = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=100)
    sku = models.CharField(max_length=20, unique=True)
    kategori = models.CharField(max_length=100)
    harga_produk = models.FloatField()
    stok = models.IntegerField()
    tanggal_masuk = models.DateTimeField()

class Suplier(models.Model):
    suplier_id = models.AutoField(primary_key=True)
    nama_suplier = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    kontak = models.CharField(max_length=20)

class Pembelian(models.Model):
    pembelian_id = models.AutoField(primary_key=True)
    Produk_id = models.ForeignKey(Produk, on_delete=models.CASCADE)
    Suplier_id = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    harga_pembelian = models.FloatField()
    tanggal_pembelian = models.DateTimeField()

class Penjualan(models.Model):
    penjualan_id = models.AutoField(primary_key=True)
    Produk_id = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    harga_penjualan = models.FloatField()
    tanggal_penjualan = models.DateTimeField()

