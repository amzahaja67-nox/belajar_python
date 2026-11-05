class Pembayaran:
    def proses_pembayaran(self, jumlah):
        print("Memproses pembayaran umum:", jumlah)

class PembayaranTunai(Pembayaran):
    def proses_pembayaran(self, jumlah):
        print("Pembayaran tunai sebesar Rp", jumlah)

class PembayaranTransfer(Pembayaran):
    def proses_pembayaran(self, jumlah):
        print("Pembayaran transfer sebesar Rp", jumlah)

daftar_pembayaran = [
    PembayaranTunai(),
    PembayaranTransfer()
]

for metode in daftar_pembayaran:
    metode.proses_pembayaran(500000)
