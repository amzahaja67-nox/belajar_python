
stack = []

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
        stack.append(data)
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        if len(stack) == 0:
            print("Stack masih kosong!")
        else:
            data = stack.pop()
            print("Data yang diambil:", data)

    elif pilihan == "3":
        if len(stack) == 0:
            print("Stack masih kosong!")
        else:
            print("Data TOP:", stack[-1])

    elif pilihan == "4":
        if len(stack) == 0:
            print("Stack masih kosong!")
        else:
            print("Isi stack:", stack)

    elif pilihan == "5":
        print("Jumlah elemen:", len(stack))

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih 1-6.")


# Pahami fungsi append(), pop(), stack[-1], len(), dan break. Lima bagian tersebut adalah inti dari program Stack ini.