def nama_function():
    print("Hello dari function")


nama_function()
nama_function()
nama_function()


def sapa_nama(nama):
    print("Hello", nama)
    print("Senang bertemu dengan Anda")


sapa_nama("Eko")
sapa_nama("Budi")


def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang", luas)


hitung_luas_persegi_panjang(10, 10)
hitung_luas_persegi_panjang(10, 20)


def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas


luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print("Luas lingkaran radius 5", luas1)
print("Luas lingkaran radius 10", luas2)


def sapa(nama, sapaan="Hello"):
    print(sapaan, nama)


sapa("Eko")
sapa("Budi", "Hi")
sapa("Joko", "Hey")


def perkenalan(nama, umur, kota):
    print("Nama", nama)
    print("Umur", umur)
    print("Kota", kota)
    print("-------")


perkenalan("Eko", 30, "Jakarta")

perkenalan(kota="Bandung", umur=25, nama="Rani")
perkenalan(umur=17, kota="Makasar", nama="Budi")


def buat_profil(nama, umur, kota="Jakarta", perkerjaan="Belum Bekerja"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"Umur = {umur} tahun")
    print(f"Kota = {kota} tahun")
    print(f"Perkerjaan = {perkerjaan}")
    print("==================")


buat_profil("Eko", 30)
buat_profil("Budi", 25, perkerjaan="Programmer")
buat_profil("Rani", 25, kota="Bandung")


def fungsi_test():
    x = 10
    print("Nilai x adalah", x)


fungsi_test()
# print(x) tidak bisa diakses dari luar, karena local variable

nama_global = "Alice"


def tampilkan_nama():
    print("Nama:", nama_global)


tampilkan_nama()


def ubah_nama():
    global nama_global
    nama_global = "Bob"
    print("Nama Local:", nama_global)


ubah_nama()
tampilkan_nama()


def cetak_list(*list):
    for item in list:
        print(item)


cetak_list(1, 2, 3, 4, 5)
cetak_list("Eko", "Budi", "Rani")

def cetak_dict(**dict):
    for key, value in dict.items():
        print(key, value)

cetak_dict(nama="Eko", umur=25, kota="Bandung")
cetak_dict(nama="Budi", umur=25, kota="Bandung")
