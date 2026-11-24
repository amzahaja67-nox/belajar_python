class Sekolah:
    def __init__(self, nama_sekolah, alamat_sekolah, jumlah_guru, jumlah_murid):
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah
        self.jumlah_guru = jumlah_guru
        self.jumlah_murid = jumlah_murid
    def tampilkan_info(self):
        print("\nNama Sekolah:", self.nama_sekolah)
        print("Alamat:", self.alamat_sekolah)
        print("Jumlah Guru:", self.jumlah_guru)
        print("Jumlah Murid:", self.jumlah_murid)

class Guru:
    def __init__(self, NIDN, nama, pelajaran, kelas):
        self.NIDN = NIDN
        self.nama = nama
        self.pelajaran = pelajaran
        self.kelas = kelas
    def tampilkan_info(self):
        print("\nNIDN:", self.NIDN)
        print("Nama:", self.nama)
        print("Pelajaran:", self.pelajaran)
        print("Kelas:", self.kelas)

class Murid:
    def __init__(self, NIS, nama, kelas):
        self.NIS = NIS
        self.nama = nama
        self.kelas = kelas
    def tampilkan_info(self):
        print("\nNIS:", self.NIS)
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)

sekolah = Sekolah("SMP Negeri 7", "Jl. Muara Bulian No. 1", 50, 50)
guru1 = Guru("0968", "Hamzah Azka", "Matematika", "3A")
guru2 = Guru("3587", "Ardiansyah", "Bahasa Inggris", "3B")
guru3 = Guru("2756", "Delendra", "Pendidikan Kewarganegaraan", "3C")
murid1 = Murid("2508", "Bedul", "3A")
murid2 = Murid("2509", "Budi", "3B")
murid3 = Murid("2510", "Bambang", "3C")

print("\n=== Informasi Sekolah ===")
sekolah.tampilkan_info()

print("\n=== Informasi Guru ===")
guru1.tampilkan_info()
guru2.tampilkan_info()
guru3.tampilkan_info()

print("\n=== Informasi Murid ===")
murid1.tampilkan_info()
murid2.tampilkan_info()
murid3.tampilkan_info()