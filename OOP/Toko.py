class Toko:
    def __init__(self, nama_toko, jumlah_pegawai, stok_produk):
        self.nama_toko = nama_toko
        self.jumlah_pegawai = jumlah_pegawai
        self.stok_produk = stok_produk
    def tampilkan_info(self):
        print("Nama Toko :", self.nama_toko)
        print("Jumlah Pegawai :", self.jumlah_pegawai)
        print("Stok Barang :", self.stok_produk)

class Pegawai:
    def __init__(self, NIP, nama, jabatan, gaji):
        self.NIP = NIP
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
    def tampilkan_info(self):
        print("\nNIP :", self.NIP)
        print("Nama :", self.nama)
        print("Jabatan :, self.jabatan")
        print("Gaji :", self.gaji)

class Produk:
    def __init__(self, kode, nama_produk, harga, stok):
        self.kode = kode
        self.nama_produk = nama_produk
        self.harga = harga
        self.stok = stok
    def tampilkan_info(self):
        print("\nKode :", self.kode)
        print("Nama Produk :", self.nama_produk)
        print("Harga :", self.harga)
        print("Stok :", self.stok)

toko1 = Toko("Toko Bagus", "2", "2")
pegawai1 = Pegawai("2345", "Azka", "kasir", "5000000")
pegawai2 = Pegawai("6789", "Fatir", "Angkut Barang", "1000000")
produk1 = Produk("0987", "sabun cuci", "2500", "100")
produk2 = Produk("6576", "sikat gigi", "5000", "50")

print("\n===INFO TOKO===")
toko1.tampilkan_info()
print("\n===INFO PEGAWAI===")
pegawai1.tampilkan_info()
pegawai2.tampilkan_info()
print("\n===INFO PRODUK===")
produk1.tampilkan_info()
produk2.tampilkan_info()