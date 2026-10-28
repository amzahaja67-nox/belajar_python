# Circular Queue Sederhana - Kapasitas 5

MAX = 5
queue = [None] * MAX
front = -1
rear = -1
jumlah = 0


def enqueue(data):
    global front, rear, jumlah

    if jumlah == MAX:
        print("Queue penuh!")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % MAX   # bergerak melingkar
    queue[rear] = data
    jumlah += 1
    print(f"Masuk : {data}")


def dequeue():
    global front, rear, jumlah

    if jumlah == 0:
        print("Queue kosong!")
        return

    data = queue[front]
    queue[front] = None
    front = (front + 1) % MAX   # bergerak melingkar
    jumlah -= 1

    if jumlah == 0:
        front = -1
        rear = -1

    print(f"Keluar: {data}")
    return data


def tampil():
    if jumlah == 0:
        print("Queue kosong")
        return

    hasil = []
    i = front
    for _ in range(jumlah):
        hasil.append(queue[i])
        i = (i + 1) % MAX

    print("Isi queue:", " -> ".join(hasil))
    print("Array    :", queue)
    print()


# ===== Program Utama =====

# 1. Masukkan A, B, C, D, E
enqueue("A")
enqueue("B")
enqueue("C")
enqueue("D")
enqueue("E")
tampil()

# 2. Ambil dua data pertama
dequeue()
dequeue()
tampil()

# 3. Masukkan F dan G
enqueue("F")
enqueue("G")
tampil()

# 4. Hasil akhir: C -> D -> E -> F -> G
