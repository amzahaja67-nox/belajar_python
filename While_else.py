# Menyiapkan password dan batas percobaan.
password_benar = "12345"
percobaan = 0
max_percobaan = 3

# Memberi kesempatan login maksimal tiga kali.
while percobaan < max_percobaan:
    password = input("Masukkan password: ")
    percobaan += 1

    if password == password_benar:
        print("Login berhasil")
        break
    else:
        print("Password salah, sisa percobaan", max_percobaan - percobaan)
else:
    print("Terlalu banyak percobaan gagal, akses ditolak")
