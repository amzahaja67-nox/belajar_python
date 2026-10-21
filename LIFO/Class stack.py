
# Membuat struktur data Stack.
class Stack:
    def __init__(self):
        # Menyimpan elemen stack dalam list.
        self.items = []

    # Menambahkan data ke bagian atas stack.
    def push(self, data):
        self.items.append(data)
        print("Data berhasil ditambahkan!")

    # Mengambil data paling atas.
    def pop(self):
        if self.is_empty():
            print("Stack masih kosong!")
        else:
            data = self.items.pop()
            print("Data yang diambil:", data)

    # Melihat data paling atas tanpa menghapusnya.
    def peek(self):
        if self.is_empty():
            print("Stack masih kosong!")
        else:
            print("Data TOP:", self.items[-1])

    # Menampilkan seluruh isi stack.
    def display(self):
        if self.is_empty():
            print("Stack masih kosong!")
        else:
            print("Isi stack:", self.items)

    # Menghitung jumlah elemen stack.
    def size(self):
        print("Jumlah elemen:", len(self.items))

    # Memeriksa apakah stack kosong.
    def is_empty(self):
        return len(self.items) == 0


# Membuat objek Stack.
stack = Stack()

# Menampilkan menu selama program berjalan.
while True:
    print("\n===== PROGRAM STACK =====")
    print("1. Push data")
    print("2. Pop data")
    print("3. Lihat TOP")
    print("4. Tampilkan seluruh data")
    print("5. Hitung jumlah elemen")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        stack.push(data)

    elif pilihan == "2":
        stack.pop()

    elif pilihan == "3":
        stack.peek()

    elif pilihan == "4":
        stack.display()

    elif pilihan == "5":
        stack.size()

    elif pilihan == "6":
        print("Program selesai.")
        break
 
    else:
        print("Pilihan tidak valid!")

# class Stack adalah cetakan untuk membuat objek Stack yang memiliki data dan fungsi sendiri.
