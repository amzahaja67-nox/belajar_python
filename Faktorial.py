# Fungsi faktorial rekursif
def factorial(n):
    if n == 0:
        return 1
    print(f"Menghitung {n} x factorial({n-1})")
    return n * factorial(n - 1)


# Program utama
try:
    angka = int(input("Masukkan bilangan: "))
    if angka < 0:
        print("Error: Bilangan tidak boleh negatif!")
    else:
        print("Hasil faktorial:", factorial(angka))
except ValueError:
    print("Error: Input harus berupa bilangan bulat!")
