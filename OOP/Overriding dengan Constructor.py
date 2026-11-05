class Pegawai:
    def __init__(self, nama):
        self.nama = nama

    def menampilkan_data(self):
        print("Nama Pegawai:", self.nama)

class Dosen(Pegawai):
    def __init__(self, nama, nidn):
        super().__init__(nama)
        self.nidn = nidn

    def menampilkan_data(self):
        super().menampilkan_data()
        print("NIDN:", self.nidn)

class TenagaKependidikan(Pegawai):
    def __init__(self, nama, bagian):
        super().__init__(nama)
        self.bagian = bagian

    def menampilkan_data(self):
        super().menampilkan_data()
        print("Bagian:", self.bagian)

dosen = Dosen("Andi", "1234567890")
tendik = TenagaKependidikan("Budi", "Administrasi")

dosen.menampilkan_data()

print()

tendik.menampilkan_data()
