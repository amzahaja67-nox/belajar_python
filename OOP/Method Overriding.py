class Hewan:
    def bersuara(self):
        print("Hewan mengeluarkan suara")

class Kucing(Hewan):
    def bersuara(self):
        print("Kucing mengeong")

class Anjing(Hewan):
    def bersuara(self):
        print("Anjing menggonggong")

# Membuat objek
kucing = Kucing()
anjing = Anjing()

# Memanggil method
kucing.bersuara()
anjing.bersuara()
