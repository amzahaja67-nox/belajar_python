class Dosen:
    def __init__(self, nama_dosen, NIP, mata_kuliah):
        self.nama_dosen = nama_dosen
        self.NIP = NIP
        self.mata_kuliah = mata_kuliah
    def tampilkan_info(self):
        print("Nama Dosen:", self.nama_dosen)
        print("NIP:", self.NIP)
        print("Mata Kuliah:", self.mata_kuliah)

dosen1 = Dosen("Dr. Hamzah Azka", "123456789", "Pemrograman Berorientasi Objek")
dosen2 = Dosen("Dr. M Fathir", "987654321", "Struktur Data")
dosen3 = Dosen("Dr. M. Azril", "456789123", "Basis Data")
print("\n===INFO DOSEN===")
dosen1.tampilkan_info()
dosen2.tampilkan_info()
dosen3.tampilkan_info()
