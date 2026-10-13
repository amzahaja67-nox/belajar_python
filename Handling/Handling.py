from pathlib import Path
import os
# Fungsi untuk membuat file data.txt
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.txt"
MAHASISWA_FILE = BASE_DIR / "mahasiswa.txt"

# Fungsi untuk membuat file data.txt
def buat_file():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        file.write("Belajar File Handling Python\n")
        file.write("Dengan baik dan benar\n")
        file.write("Menggunakan Visual Studio Code")
    print("File berhasil dibuat")

# Fungsi untuk membaca file data.txt
def baca_file():
    if not DATA_FILE.exists():
        print("File data.txt belum dibuat.")
        return

    with DATA_FILE.open("r", encoding="utf-8") as file:
        isi = file.read()
        print("\nIsi file data.txt:\n")
        print(isi)

# Fungsi untuk membaca file per baris
def baca_per_baris():
    if not DATA_FILE.exists():
        print("File data.txt belum dibuat.")
        return

    with DATA_FILE.open("r", encoding="utf-8") as file:
        print("\nIsi file per baris:\n")
        for baris in file:
            print(baris, end="")

# Fungsi untuk menambahkan data ke file data.txt
def tambah_data():
    if not DATA_FILE.exists():
        print("File data.txt belum dibuat. Silakan buat file terlebih dahulu.")
        return

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write("\nPraktikum Python")

    print("Data berhasil ditambahkan")

# Fungsi untuk mengecek keberadaan file
def cek_file():
    if DATA_FILE.exists():
        print("File data.txt ditemukan")
    else:
        print("File data.txt tidak ditemukan")

    if MAHASISWA_FILE.exists():
        print("File mahasiswa.txt ditemukan")
    else:
        print("File mahasiswa.txt tidak ditemukan")

# Fungsi untuk menghitung jumlah baris dalam file mahasiswa.txt
def hitung_jumlah_baris():
    if not MAHASISWA_FILE.exists():
        print("File mahasiswa.txt belum dibuat.")
        return

    with MAHASISWA_FILE.open("r", encoding="utf-8") as file:
        jumlah = len(file.readlines())

    print(f"Jumlah data : {jumlah}")

# Fungsi untuk menyimpan data mahasiswa ke file mahasiswa.txt
def simpan_data_mahasiswa():
    nama = input("Masukkan nama : ")
    nim = input("Masukkan NIM : ")
    ttl = input("Masukkan tempat tanggal lahir : ")

    with MAHASISWA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{nama} - {nim} - {ttl}\n")

    print("Data berhasil disimpan")

    lanjut = input("Apakah Anda ingin memasukkan data lagi? (y/n): ")
    while lanjut.lower() == "y":
        nama = input("Masukkan nama : ")
        nim = input("Masukkan NIM : ")
        ttl = input("Masukkan tempat tanggal lahir : ")

        with MAHASISWA_FILE.open("a", encoding="utf-8") as file:
            file.write(f"{nama} - {nim} - {ttl}\n")

        print("Data berhasil disimpan")
        lanjut = input("Apakah Anda ingin memasukkan data lagi? (y/n): ")

# Fungsi untuk menampilkan data mahasiswa dari file mahasiswa.txt
def tampilkan_data_mahasiswa():
    if not MAHASISWA_FILE.exists():
        print("File mahasiswa.txt belum dibuat.")
        return

    with MAHASISWA_FILE.open("r", encoding="utf-8") as file:
        print("\nData mahasiswa:\n")
        print(file.read())

# Fungsi untuk menghapus file data.txt
def hapus_file():
    if DATA_FILE.exists():
        os.remove(DATA_FILE)
        print("File data.txt berhasil dihapus")
    else:
        print("File data.txt tidak ditemukan")

# Fungsi untuk menjalankan semua contoh
def jalankan_semua_contoh():
    print("\n=== Membuat file data.txt ===")
    buat_file()

    print("\n=== Membaca file data.txt ===")
    baca_file()

    print("\n=== Membaca file per baris ===")
    baca_per_baris()

    print("\n=== Menambahkan data ke file ===")
    tambah_data()

    print("\n=== Mengecek file ===")
    cek_file()

    print("\n=== Menampilkan data mahasiswa ===")
    tampilkan_data_mahasiswa()

    print("\n=== Menghitung jumlah baris ===")
    hitung_jumlah_baris()

    print("\n=== Simpan data mahasiswa ===")
    simpan_data_mahasiswa()

    print("\n=== Menampilkan data mahasiswa ===")
    tampilkan_data_mahasiswa()

# Fungsi untuk menampilkan menu
def menu():
    print("\n=== PROGRAM FILE HANDLING PYTHON ===")
    print("1. Buat file data.txt")
    print("2. Baca file data.txt")
    print("3. Baca per baris")
    print("4. Tambah data ke data.txt")
    print("5. Cek keberadaan file")
    print("6. Hitung jumlah baris mahasiswa.txt")
    print("7. Simpan data mahasiswa")
    print("8. Tampilkan data mahasiswa")
    print("9. Hapus file data.txt")
    print("10. Jalankan semua contoh")
    print("0. Keluar")

# Fungsi untuk menjalankan program
def main():
    while True:
        menu()
        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            buat_file()
        elif pilihan == "2":
            baca_file()
        elif pilihan == "3":
            baca_per_baris()
        elif pilihan == "4":
            tambah_data()
        elif pilihan == "5":
            cek_file()
        elif pilihan == "6":
            hitung_jumlah_baris()
        elif pilihan == "7":
            simpan_data_mahasiswa()
        elif pilihan == "8":
            tampilkan_data_mahasiswa()
        elif pilihan == "9":
            hapus_file()
        elif pilihan == "10":
            jalankan_semua_contoh()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
