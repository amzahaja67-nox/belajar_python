class Rumah_Sakit:
    def __init__(self, nama, alamat, jumlah_kamar, jumlah_dokter):
        self.nama = nama
        self.alamat = alamat
        self.jumlah_kamar = jumlah_kamar
        self.jumlah_dokter = jumlah_dokter
    def tampilkan_info(self):
        print("Nama Rumah Sakit :", self.nama)
        print("Alamat :", self.alamat)
        print("Jumlah Kamar :", self.jumlah_kamar)
        print("Jumlah Dokter :", self.jumlah_dokter)

class Dokter:
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi
    def tampilkan_info(self):
        print("Nama Dokter :", self.nama)
        print("Spesialisasi :", self.spesialisasi)

class Pasien:
    def __init__(self, nama, umur, penyakit):
        self.nama = nama
        self.umur = umur
        self.penyakit = penyakit
    def tampilkan_info(self):
        print("Nama Pasien :", self.nama)
        print("Umur :", self.umur)
        print("Penyakit :", self.penyakit)

rumah_sakit = Rumah_Sakit("RS H.Hamzah", "Jl. Muara Bulian No. 25", 20, 5)
dokter1 = Dokter("Dr. Fathir", "Spesialis Gigi")
dokter2 = Dokter("Dr. Kemaz", "Spesialis Mata")
dokter3 = Dokter("Dr. Arifin", "Spesialis Jantung")
dokter4 = Dokter("Dr. Fadil", "Spesialis Kulit")
dokter5 = Dokter("Dr. Alan", "Spesialis Anak")
pasien1 = Pasien("Ridho", 19, "Demam")
pasien2 = Pasien("Ilham", 20, "Mata")
pasien3 = Pasien("Indra", 21, "Gigi")

print("=== INFORMASI RUMAH SAKIT ===")
rumah_sakit.tampilkan_info()
print("\n=== INFORMASI DOKTER ===")
dokter1.tampilkan_info()
dokter2.tampilkan_info()
dokter3.tampilkan_info()
dokter4.tampilkan_info()
dokter5.tampilkan_info()
print("\n=== INFORMASI PASIEN ===")
pasien1.tampilkan_info()
pasien2.tampilkan_info()
pasien3.tampilkan_info()