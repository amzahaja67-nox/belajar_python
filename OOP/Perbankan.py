class Bank:
    def __init__(self, nama_bank, alamat, kode_bank, daftar_rekening, jumlah_karyawan):
        self.nama_bank = nama_bank
        self.alamat = alamat
        self.kode_bank = kode_bank
        self.daftar_rekening = daftar_rekening
        self.jumlah_karyawan = jumlah_karyawan
    def tampilkan_info(self):
        print("\nNama Bank :", self.nama_bank)
        print("Alamat :", self.alamat)
        print("Kode Bank :", self.kode_bank)
        print("Jumlah Rekening :", len(self.daftar_rekening))
        print("Jumlah Karyawan :", self.jumlah_karyawan)

class Rekening:
    def __init__(self, nomor_rekening, nama_pemilik, saldo):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo
    def tampilkan_info(self):
        print("\nNomor Rekening :", self.nomor_rekening)
        print("Nama Pemilik :", self.nama_pemilik)
        print("Saldo :", self.saldo)

class Karyawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
    def tampilkan_info(self):
        print("\nNama Karyawan :", self.nama)
        print("Jabatan :", self.jabatan)
        print("Gaji :", self.gaji)

class Nasabah:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
    def tampilkan_info(self):
        print("\nNama Nasabah :", self.nama)
        print("Alamat :", self.alamat)
        print("Nomor Telepon :", self.nomor_telepon)

bank = Bank("Bank AMZ", "Jl. Muara Bulian No. 09", "HAM025", [], 4)

rekening = Rekening("1234567890", "Azka", 1000000)
rekening2 = Rekening("0987654321", "Hamzah", 500000)
rekening3 = Rekening("1122334455", "Fathir", 750000)
rekening4 = Rekening("5566778899", "Kemaz", 250000)

karyawan1 = Karyawan("Amzah", "Manager", 5500000)
karyawan2 = Karyawan("Indra", "Staff01", 3400000)
karyawan3 = Karyawan("Fathir", "Staff02", 3400000)
karyawan4 = Karyawan("Kemaz", "Security", 3000000)

nasabah1 = Nasabah("Ridho", "Jl. Muara Bulian No. 09", "081234567890")
nasabah2 = Nasabah("Iham", "Jl. Muara Bulian No. 10", "081234567891")

print("=== INFORMASI BANK ===")
bank.tampilkan_info()

print("\n=== INFORMASI REKENING ===")
rekening.tampilkan_info()
rekening2.tampilkan_info()
rekening3.tampilkan_info()
rekening4.tampilkan_info()

print("\n=== INFORMASI KARYAWAN ===")
karyawan1.tampilkan_info()
karyawan2.tampilkan_info()
karyawan3.tampilkan_info()
karyawan4.tampilkan_info()

print("\n=== INFORMASI NASABAH ===")
nasabah1.tampilkan_info()
nasabah2.tampilkan_info()