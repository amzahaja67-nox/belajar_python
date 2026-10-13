class Sekolah:
    def __init__(self, nama_sekolah, alamat, jumlah_guru, jumlah_murid):
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.jumlah_guru = jumlah_guru
        self.jumlah_murid = jumlah_murid
    def tampilkan_info(self):
        print("Nama Sekolah :", self.nama_sekolah)
        print("Alamat :", self.alamat)
        print("Jumlah Guru :", self.jumlah_guru)
        print("Jumlah Murid :", self.jumlah_murid)

class Dosen:
    def __init__(self, nama, pelajaran):
        self.nama = nama
        self.pelajaran = pelajaran
    def tampilkan_info(self):
        print("Nama :", self.nama)
        print("Pelajaran :", self.pelajaran)

class Mahasiswa:
    def __init__(self, nama, nim, )