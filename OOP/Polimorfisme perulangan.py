class Hewan:
    def bersuara(self):
        print("Hewan mengeluarkan suara")

class Kucing(Hewan):
    def bersuara(self):
        print("Meong...")

class Anjing(Hewan):
    def bersuara(self):
        print("Guk guk...")

class Sapi(Hewan):
    def bersuara(self):
        print("Mooo...")

# Membuat kumpulan objek
daftar_hewan = [
    Kucing(),
    Anjing(),
    Sapi()
]

# Polimorfisme
for hewan in daftar_hewan:
    hewan.bersuara()
