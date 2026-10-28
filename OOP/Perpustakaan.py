# Menyimpan informasi perpustakaan.
class Perpustakaan:
    def __init__(self, nama_perpustakaan, alamat, jumlah_buku):
        self.nama_perpustakaan = nama_perpustakaan
        self.alamat = alamat
        self.jumlah_buku = jumlah_buku
    def tampilkan_info(self):
        print("\nNama Perpustakaan :", self.nama_perpustakaan)
        print("Alamat :", self.alamat)
        print("Jumlah Buku :", self.jumlah_buku)
        
# Menyimpan informasi buku.
class Buku:
    def __init__(self, judul_buku, pencipta, tahun_terbit):
        self.judul_buku = judul_buku
        self.pencipta = pencipta
        self.tahun_terbit = tahun_terbit
    def tampilkan_info(self):
        print("\nJudul Buku :", self.judul_buku)
        print("Pencipta :", self.pencipta)
        print("Tahun Terbit :", self.tahun_terbit)

# Menyimpan informasi anggota.
class Anggota:
    def __init__(self, nama, nim, alamat, nomor_handphone):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.nomor_handphone = nomor_handphone
    def tampilkan_info(self):
        print("\nNama :", self.nama)
        print("NIM :", self.nim)
        print("Alamat :", self.alamat)
        print("Nomor Handphone :", self.nomor_handphone)

# Membuat data contoh perpustakaan, buku, dan anggota.
perpustakaan = Perpustakaan("Perpustakaan Amzah", "Jl. Muara Bulian No. 1", 5)

buku1 = Buku("Sistem Basis Data", "Indra", 2020)
buku2 = Buku("Pemrograman Dasar", "Fathir", 2021)
buku3 = Buku("Dasar Dasar Python", "Ilham", 2025)
buku4 = Buku("Bahasa Indonesia", "Azka", 2022)
buku5 = Buku("Bahasa Inggris", "Dhani", 2023)

anggota1 = Anggota("Kemaz", "251010146100081", "Jl. Muara Bulian No. 01", "081234567890")
anggota2 = Anggota("Azka", "251010146100082", "Jl. Muara Bulian No. 02", "081234567891")
anggota3 = Anggota("Alan", "251010146100083", "Jl. Muara Bulian No. 03", "081234567892")
anggota4 = Anggota("Delendra", "251010146100084", "Jl. Muara Bulian No. 04", "081234567893")
anggota5 = Anggota("Rizky", "251010146100085", "Jl. Muara Bulian No. 05", "081234567894")

print("===INFO PERPUSTAKAAN===")
perpustakaan.tampilkan_info()

print("\n===INFO BUKU===")
buku1.tampilkan_info()
buku2.tampilkan_info()
buku3.tampilkan_info()
buku4.tampilkan_info()
buku4.tampilkan_info()
buku5.tampilkan_info()

print("\n===INFO ANGGOTA===")
anggota1.tampilkan_info()
anggota2.tampilkan_info()
anggota3.tampilkan_info()
anggota4.tampilkan_info()
anggota5.tampilkan_info()
