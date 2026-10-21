# Menyimpan angka rahasia.
angka_rahasia = 1576

# Meminta tebakan sampai jawaban benar.
while True:
    tebakan = int(input("Masukkan tebakan: "))
    if tebakan == angka_rahasia:
        print("selamat, Anda benar")
        break
    else:
        print("Salah, coba lagi")
