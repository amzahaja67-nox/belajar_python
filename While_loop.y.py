# Menampilkan angka 1 sampai 5.
angka = 1
while angka <= 5:
    print(angka)
    angka += 1  # Menambah angka agar perulangan berlanjut.

# Mengulang input sampai password benar.
password = "hamzah25"

while password != "12345":
    password = input("Masukkan password : ")
    if password != "12345":
        print("Password salah")

print("Password benar")
