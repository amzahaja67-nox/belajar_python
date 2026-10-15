class Sekolah:
    def __init__(self, nama_sekolah, alamat, jumlah_guru, jumlah_murid):
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.jumlah_guru = jumlah_guru
        self.jumlah_murid = jumlah_murid
    def tampilkan_info(self):
        print("\nNama Sekolah :", self.nama_sekolah)
        print("Alamat :", self.alamat)
        print("Jumlah Guru :", self.jumlah_guru)
        print("Jumlah Murid :", self.jumlah_murid)

class Guru:
    def __init__(self, nama, pelajaran):
        self.nama = nama
        self.pelajaran = pelajaran
    def tampilkan_info(self):
        print("\nNama :", self.nama)
        print("Pelajaran :", self.pelajaran)

class Siswa:
    def __init__(self, nama, nim, ):
        self.nama = nama
        self.nim = nim
    def tampilkan_info(self):
        print("\nNama :", self.nama)
        print("NIM :", self.nim)

sekolah1 = Sekolah("SD N 176", "JL. Muara Bulian", "2", "2")
guru1 = Guru("azka", "PBO", "Pemrograman")
guru2 = Guru("fatir", "figma")
siswa1 = Siswa("kemaz", "12345")
siswa2 = Siswa("Fadil", "67890")

print("===INFO SEKOLAH===")
sekolah1.tampilkan_info()
print("==INFO GURU===")
guru1.tampilkan_info()
guru2.tampilkan_info()
print("===INFO SISWA===")
siswa1.tampilkan_info()
siswa2.tampilkan_info()