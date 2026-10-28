antrean = []

# Menambahkan lima mahasiswa
antrean.append("MHS-001")
antrean.append("MHS-002")
antrean.append("MHS-003")
antrean.append("MHS-004")
antrean.append("MHS-005")

# Menampilkan antrean awal
print("Antrean awal:", antrean)
print("Jumlah antrean:", len(antrean))

# Melayani dua mahasiswa (dequeue)
mahasiswa_dilayani = antrean.pop(0)
print("\nDilayani:", mahasiswa_dilayani)
print("Jumlah antrean:", len(antrean))

mahasiswa_dilayani = antrean.pop(0)
print("\nDilayani:", mahasiswa_dilayani)
print("Jumlah antrean:", len(antrean))

# Menambahkan mahasiswa baru
antrean.append("MHS-006")

# Menampilkan antrean terakhir
print("\nAntrean terakhir:", antrean)
print("Elemen terdepan:", antrean[0])
print("Elemen paling belakang:", antrean[-1])
print("Jumlah antrean:", len(antrean))