class Dosen:
    def __init__(self, nama_dosen, NIP, mata_kuliah):
        self.nama_dosen = nama_dosen
        self.NIP = NIP
        self.mata_kuliah = mata_kuliah
    def tampilkan_info(self):
        print("Nama Dosen:", self.nama_dosen)
        print("NIP:", self.NIP)
        print("Mata Kuliah:", self.mata_kuliah)

dosen = Dosen("Dr. Hamzah Azka", "123456789", "Pemrograman Berorientasi Objek")
print("\n===INFO DOSEN===")
dosen.tampilkan_info()
