class Dosen:
    def __init__(self, NIDN, nama, prodi):
        self.NIDN = NIDN
        self.nama = nama
        self.prodi = prodi
    def tampilkan_info(self):
        print("\nNIDN :", self.NIDN)
        print("Nama :", self.nama)
        print("Prodi :", self.prodi)

dosen = Dosen("251010", "Azka", "Sistem Informasi")
print("\n===INFO DOSEN===")
dosen.tampilkan_info()