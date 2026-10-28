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
print("Front:", antrean[0])
print("Rear:", antrean[-1])

# Melayani mahasiswa pertama (dequeue)
mahasiswa_dilayani = antrean.pop(0)
print("\nDilayani:", mahasiswa_dilayani)
print("Jumlah antrean:", len(antrean))
print("Front:", antrean[0])
print("Rear:", antrean[-1])

# Melayani mahasiswa kedua (dequeue)
mahasiswa_dilayani = antrean.pop(0)
print("\nDilayani:", mahasiswa_dilayani)
print("Jumlah antrean:", len(antrean))
print("Front:", antrean[0])
print("Rear:", antrean[-1])

# Menambahkan mahasiswa baru (enqueue)
antrean.append("MHS-006")

# Menampilkan antrean terakhir
print("\nAntrean terakhir:", antrean)
print("Front:", antrean[0])
print("Rear:", antrean[-1])
print("Jumlah antrean:", len(antrean))