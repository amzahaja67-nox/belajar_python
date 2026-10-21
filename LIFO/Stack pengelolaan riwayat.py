
class Stack:
    def __init__(self):
        self.aktivitas = []

    # Menambahkan aktivitas
    def push(self, data):
        self.aktivitas.append(data)
        print("Aktivitas berhasil ditambahkan!")

    # Mengambil aktivitas terakhir
    def pop(self):
        if self.is_empty():
            print("Stack kosong! Tidak ada aktivitas yang bisa diambil.")
        else:
            data = self.aktivitas.pop()
            print("Aktivitas yang diambil:", data)

    # Menampilkan seluruh aktivitas
    def display(self):
        if self.is_empty():
            print("Belum ada aktivitas yang tersimpan.")
        else:
            print("\nRiwayat Aktivitas:")
            for i, data in enumerate(self.aktivitas, start=1):
                print(f"{i}. {data}")

    # Memeriksa apakah stack kosong
    def is_empty(self):
        return len(self.aktivitas) == 0

    # Menghitung jumlah aktivitas
    def size(self):
        return len(self.aktivitas)


# Membuat objek Stack
stack = Stack()

# Menu aplikasi
while True:
    print("\n======================================")
    print(" PENGELOLAAN RIWAYAT AKTIVITAS")
    print("       OPERATOR AKADEMIK")
    print("======================================")
    print("1. Tambah aktivitas")
    print("2. Tampilkan riwayat aktivitas")
    print("3. Ambil aktivitas terakhir")
    print("4. Periksa stack kosong")
    print("5. Hitung jumlah aktivitas")
    print("6. Keluar")
    print("======================================")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        # Meminta nama aktivitas baru.
        data = input("Masukkan nama aktivitas: ")

        if data.strip() == "":
            print("Aktivitas tidak boleh kosong.")
        else:
            stack.push(data)

    elif pilihan == "2":
        stack.display()

    elif pilihan == "3":
        stack.pop()

    elif pilihan == "4":
        if stack.is_empty():
            print("Stack dalam keadaan kosong.")
        else:
            print("Stack berisi aktivitas.")

    elif pilihan == "5":
        print("Jumlah aktivitas:", stack.size())

    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")
