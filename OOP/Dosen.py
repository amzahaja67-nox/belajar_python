# Menyimpan informasi dosen.
class Dosen:
    def __init__(self, NIDN, nama, kelas, prodi):
        self.NIDN = NIDN
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
    def tampilkan_info(self):
        print("\nNIDN :", self.NIDN)
        print("Nama :", self.nama)
        print("Kelas :", self.kelas)
        print("Prodi :", self.prodi)

# Membuat objek dosen.
dosen = Dosen("251010", "M Fathir", "3", "Sistem Informasi")

print("\n===INFO DOSEN===")
dosen.tampilkan_info()
