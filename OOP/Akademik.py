class Kampus:
    def __init__(self, nama_kampus, alamat_kampus, jumlah_dosen, jumlah_mahasiswa):
        self.nama_kampus = nama_kampus
        self.alamat_kampus = alamat_kampus
        self.jumlah_dosen = jumlah_dosen
        self.jumlah_mahasiswa = jumlah_mahasiswa
    def tampilkan_info(self):
        print("\nNama kampus :", self.nama_kampus)
        print("Alamat kampus :", self.alamat_kampus)
        print("Jumlah dosen :", self.jumlah_dosen)
        print("Jumlah mahasiswa :", self.jumlah_mahasiswa)

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

class Mahasiswa:
    def __init__(self, NIM, nama, semester, prodi):
        self.NIM = NIM
        self.nama = nama
        self.semester = semester
        self.prodi = prodi
    def tampilkan_info(self):
        print("\nNIM :", self.NIM)
        print("Nama :", self.nama)
        print("Semester :", self.semester)
        print("Prodi :", self.prodi)

kampus = Kampus("Universitas Graha Karya Muara Bulian", "Jl. Teratai No. 123", 50, 2000)
dosen1 = Dosen("001", "Dr. Hamzah Azka", "A", "Teknik Informatika")
dosen2 = Dosen("002", "Dr. M Fathir", "B", "Sistem Informasi")
dosen3 = Dosen("003", "Dr. M. Azril", "C", "Teknik Elektro")
mahasiswa1 = Mahasiswa("123456789", "Kemaz Raihan", 3, "Sistem Informasi")
mahasiswa2 = Mahasiswa("987654321", "Rizky Fadillah", 5, "Teknik Informatika")
mahasiswa3 = Mahasiswa("456789123", "Ridho Rhoma", 7, "Teknik Elektro")
print("\n===INFO KAMPUS===")
kampus.tampilkan_info()
print("\n===INFO DOSEN===")
dosen1.tampilkan_info()
dosen2.tampilkan_info()
print("\n===INFO MAHASISWA===")
mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()