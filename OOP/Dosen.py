class dosen:
    def __init__(self, NIDN, nama, prodi):
        self.NIDN = NIDN
        self.nama = nama
        self.prodi = prodi
    def tampilkan_info(self):
        print("\nNIDN :", self.NIDN)
        print("Nama :", self.nama)
        print("Prodi :", self.prodi)

dosen1 = dosen("1234567890", "Pak Hendra", "PBO")
dosen2 = dosen("0987654321", "Pak Finur", "Pemrograman Dasar")

print("=== INFORMASI DOSEN ===")
dosen1.tampilkan_info()
dosen2.tampilkan_info()