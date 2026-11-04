# Panduan Belajar Dasar Pemrograman Python & Struktur Data

Kumpulan contoh kode dan program latihan praktis untuk mempelajari dasar-dasar pemrograman Python, algoritma rekursif, struktur data (Stack, Queue, Pohon Biner), pengelolaan file (*file handling*), serta Pemrograman Berorientasi Objek (*Object-Oriented Programming* / OOP) secara bertahap dan terstruktur.

---

## Daftar Isi

- [Materi yang Dipelajari](#materi-yang-dipelajari)
- [Struktur Folder dan Penjelasan File](#struktur-folder-dan-penjelasan-file)
  - [1. Dasar Python dan Kontrol Alur (Root)](#1-dasar-python-dan-kontrol-alur-root)
  - [2. Algoritma Rekursi & Pohon Biner (Root)](#2-algoritma-rekursi--pohon-biner-root)
  - [3. Struktur Data Stack - LIFO (`LIFO/`)](#3-struktur-data-stack---lifo-lifo)
  - [4. Struktur Data Queue - FIFO (`Queue/`)](#4-struktur-data-queue---fifo-queue)
  - [5. Pengelolaan File (`Handling/`)](#5-pengelolaan-file-handling)
  - [6. Pemrograman Berorientasi Objek (`OOP/`)](#6-pemrograman-berorientasi-objek-oop)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Rekomendasi Urutan Belajar](#rekomendasi-urutan-belajar)
- [Tujuan Pembelajaran](#tujuan-pembelajaran)

---

## Materi yang Dipelajari

1. **Sintaks Dasar & Interaktivitas**: Menampilkan teks ke terminal, variabel, tipe data (`int`, `float`, `str`, `bool`), operasi matematika, dan menangani input dari pengguna.
2. **Kontrol Alur (Flow Control)**: Percabangan (`if`, `elif`, `else`) serta perulangan (`for`, `while`, pemanfaatan `break`, `continue`, `for-else`, dan `while-else`).
3. **Koleksi & Fungsi**: Manipulasi list/array (menambah, menyisipkan, mengubah, dan menghapus elemen) serta deklarasi fungsi kustom dengan parameter dan nilai kembalian (*return value*).
4. **Algoritma & Rekursi**: Algoritma pencarian linear (*linear search*), fungsi faktorial rekursif dengan penanganan error, serta pembuatan deret Fibonacci menggunakan rekursi biasa dan teknik *memoization*.
5. **Struktur Data Linear (LIFO & FIFO)**:
   - **Stack (LIFO - Last In, First Out)**: Implementasi menggunakan list bawaan maupun *class*, lengkap dengan studi kasus sistem riwayat aktivitas.
   - **Queue (FIFO - First In, First Out)**: Implementasi antrean berbasis list, *linked list*, serta *circular queue* (antrean melingkar berbasis array modulo).
6. **Struktur Data Non-Linear (Tree)**: Pohon Biner (*Binary Tree*) beserta teknik penelusuran (*traversal*): Preorder, Inorder, dan Postorder.
7. **Pengelolaan File (File Handling)**: Operasi pembuatan berkas (*create*), pembacaan (*read*), penambahan data (*append*), penghapusan berkas (*delete*), serta mini-project pengelolaan data mahasiswa.
8. **Object-Oriented Programming (OOP)**: Konsep *class*, atribut, *constructor* (`__init__`), *method*, dan instansiasi objek melalui berbagai studi kasus nyata (akademik, perbankan, perpustakaan, rumah sakit, dan toko).

---

## Struktur Folder dan Penjelasan File

### 1. Dasar Python dan Kontrol Alur (Root)

| File | Deskripsi Materi |
| --- | --- |
| `Hello.py` | Program pengenalan: mencetak teks sederhana ke konsol |
| `Variabel.py` | Deklarasi variabel, penetapan nilai, dan kalkulasi dasar |
| `Tipe_data.py` | Pengenalan berbagai tipe data: Integer, Float, String, dan Boolean |
| `Input.py` | Mengambil masukan interaktif dari pengguna melalui terminal |
| `If_else.py` | Struktur percabangan logika kondisi `if`, `elif`, dan `else` |
| `Perulangan.py` | Perulangan sekuensial angka menggunakan fungsi `range()` |
| `For_string.py` | Iterasi karakter demi karakter pada tipe data String |
| `For_else.py` | Mekanisme pencarian data memanfaatkan blok `for-else` |
| `While_loop.y.py` | Perulangan berbasis kondisi `while` dan simulasi validasi input kata sandi |
| `While_else.py` | Penggunaan blok `while-else` untuk membatasi jumlah percobaan input |
| `Break.py` | Menghentikan paksa iterasi perulangan dengan pernyataan `break` |
| `Continue.py` | Melewati iterasi saat ini dan lanjut ke iterasi berikutnya dengan `continue` |
| `Array.py` | Operasi manipulasi list (`insert()`, ubah indeks, `append()`, dan `remove()`) |
| `Function.py` | Pembuatan fungsi dengan parameter, argumen default, dan *return value* |
| `Data_dan_algoritma.py` | Penerapan algoritma *linear search* untuk mencari indeks target dalam list |

### 2. Algoritma Rekursi & Pohon Biner (Root)

| File | Deskripsi Materi |
| --- | --- |
| `Faktorial.py` | Perhitungan faktorial dengan rekursi serta validasi input bilangan bulat positif |
| `Fibonacci.py` | Pembentukan deret bilangan Fibonacci menggunakan rekursi standar dan rekursi dengan *memoization* |
| `Traversal  Pohon Biner.py` | Implementasi simpul (*Node*) Pohon Biner dan traversal Preorder, Inorder, dan Postorder |

### 3. Struktur Data Stack - LIFO (`LIFO/`)

| File | Deskripsi Materi |
| --- | --- |
| `LIFO/List.py` | Simulasi menu interaktif Stack LIFO menggunakan list bawaan (`append()`, `pop()`, intip elemen atas) |
| `LIFO/Class stack.py` | Implementasi struktur data Stack berbasis Class OOP lengkap dengan menu interaktif |
| `LIFO/Stack pengelolaan riwayat.py` | Studi kasus riwayat aktivitas operator akademik menggunakan konsep Stack |

### 4. Struktur Data Queue - FIFO (`Queue/`)

| File | Deskripsi Materi |
| --- | --- |
| `Queue/List_python.py` | Implementasi antrean FIFO sederhana menggunakan *class* dan list Python (`enqueue`, `dequeue`, `front`, `rear`) |
| `Queue/Queue_list.py` | Contoh class antrean FIFO berbasis list untuk pengujian antrean tiket |
| `Queue/Latihan_queue_FIFO.py` | Latihan antrean mahasiswa menggunakan operasi dasar list (`append()` dan `pop(0)`) |
| `Queue/Tugas_queue.py` | Tugas simulasi antrean pendaftaran mahasiswa beserta pengecekan elemen *front*, *rear*, dan jumlah antrean |
| `Queue/Linked_list.py` | Implementasi antrean dinamis berbasis *Linked List* (`Node` bertaut tanpa batasan kapasitas tetap) |
| `Queue/Circular_queue.py` | Antrean melingkar (*Circular Queue*) prosedural dengan batas kapasitas (modulo *indexing*) |
| `Queue/Circular_queue_Array.py` | Implementasi *Circular Queue* berbasis Class OOP menggunakan list fixed-size dan penanganan kondisi *full*/*empty* |

### 5. Pengelolaan File (`Handling/`)

| File | Deskripsi Materi |
| --- | --- |
| `Handling/Handling.py` | Program menu interaktif untuk membuat berkas, membaca seluruh teks, membaca baris per baris, menambahkan data (*append*), menghapus berkas, serta sistem sederhana pendataan mahasiswa |

### 6. Pemrograman Berorientasi Objek (`OOP/`)

| File | Deskripsi Materi |
| --- | --- |
| `OOP/Akademik.py` | Class `Kampus` untuk memodelkan informasi nama kampus, alamat, jumlah dosen, dan jumlah mahasiswa |
| `OOP/Dosen.py` | Class `Dosen` untuk menyimpan identitas dosen (NIDN, nama, kelas, prodi) |
| `OOP/Hitung nilai.py` | Modul perhitungan nilai akhir mahasiswa dengan sistem bobot nilai (Tugas 30%, UTS 30%, UAS 40%) |
| `OOP/Perbankan.py` | Class `Bank` untuk memodelkan sistem perbankan, kode bank, dan daftar rekening nasabah |
| `OOP/Perpustakaan.py` | Class `Perpustakaan` untuk mengelola data fasilitas perpustakaan dan jumlah buku |
| `OOP/Rumah_sakit.py` | Class `Rumah_Sakit` untuk merepresentasikan nama rumah sakit, alamat, kapasitas kamar, dan jumlah dokter |
| `OOP/Toko.py` | Class `Toko` untuk manajemen nama toko, staf karyawan, dan ketersediaan stok barang |

---

## Cara Menjalankan Program

### Prasyarat
Pastikan Python 3 sudah terpasang di komputer Anda. Anda dapat mengeceknya lewat terminal:
```bash
python --version
```

### Menjalankan File
Buka terminal atau command prompt pada folder proyek ini, lalu jalankan file yang diinginkan menggunakan perintah `python`:

1. **Menjalankan contoh dasar:**
   ```bash
   python Hello.py
   python Variabel.py
   python Input.py
   ```

2. **Menjalankan algoritma rekursi dan struktur data pohon:**
   ```bash
   python Faktorial.py
   python Fibonacci.py
   python "Traversal  Pohon Biner.py"
   ```
   *(Gunakan tanda petik dua jika nama file mengandung spasi)*

3. **Menjalankan program Stack (LIFO):**
   ```bash
   python "LIFO/Class stack.py"
   python "LIFO/Stack pengelolaan riwayat.py"
   ```

4. **Menjalankan program Queue (FIFO):**
   ```bash
   python Queue/Latihan_queue_FIFO.py
   python Queue/Circular_queue.py
   python Queue/Circular_queue_Array.py
   python Queue/Linked_list.py
   ```

5. **Menjalankan program File Handling dan OOP:**
   ```bash
   python Handling/Handling.py
   python OOP/Akademik.py
   python OOP/Perbankan.py
   ```

> [!NOTE]
> Beberapa file merupakan program menu interaktif yang meminta input dari pengguna (seperti `Input.py`, `Handling/Handling.py`, program di folder `LIFO/`, `Faktorial.py`, dan `Fibonacci.py`). Ikuti petunjuk menu yang tertera pada layar terminal saat program dijalankan.

---

## Rekomendasi Urutan Belajar

Agar proses pemahaman berjalan optimal, disarankan mempelajari materi dengan urutan alur berikut:

```
[Dasar & Sintaks] ➔ [Kontrol Alur & Loop] ➔ [List & Fungsi] ➔ [Pencarian & Rekursi]
                                                                        │
[OOP / Berorientasi Objek] 🠔 [File Handling] 🠔 [Tree Traversal] 🠔 [Stack & Queue]
```

1. **Tahap 1: Fondasi Bahasa**
   - Mulai dari `Hello.py`, `Variabel.py`, `Tipe_data.py`, dan `Input.py`.
2. **Tahap 2: Pengambilan Keputusan & Perulangan**
   - Pahami `If_else.py`, dilanjutkan dengan `Perulangan.py`, `For_string.py`, dan `While_loop.y.py`.
   - Perdalam kontrol iterasi dengan `Break.py`, `Continue.py`, `For_else.py`, dan `While_else.py`.
3. **Tahap 3: Koleksi Data & Modularitas Kode**
   - Pelajari manipulasi list di `Array.py` dan pembungkusan logika di `Function.py`.
4. **Tahap 4: Algoritma Pencarian & Pemikiran Rekursif**
   - Pelajari `Data_dan_algoritma.py` (Linear Search).
   - Masuk ke konsep fungsi rekursif di `Faktorial.py` serta optimasi algoritma di `Fibonacci.py` (Memoization).
5. **Tahap 5: Struktur Data Linear (Stack & Queue)**
   - Pahami konsep LIFO melalui berkas di dalam folder `LIFO/`.
   - Pahami konsep FIFO, Linked Queue, dan Circular Queue di dalam folder `Queue/`.
6. **Tahap 6: Struktur Data Hirarkis (Non-Linear)**
   - Pelajari simpul dan penelusuran pohon biner di `Traversal  Pohon Biner.py`.
7. **Tahap 7: Persistensi Data (File Handling)**
   - Pelajari cara membaca, menulis, dan memanipulasi berkas fisik di `Handling/Handling.py`.
8. **Tahap 8: Pemrograman Berorientasi Objek (OOP)**
   - Pelajari konsep dasar *class* dan perancangan entitas pada contoh-contoh di dalam folder `OOP/`.

---

## Tujuan Pembelajaran

Setelah menyelesaikan dan mempraktikkan seluruh materi pada repositori ini, Anda diharapkan mampu:

- Menguasai sintaks dasar dan alur logika pemrograman Python secara mandiri.
- Mengimplementasikan konsep perulangan, percabangan, fungsi, dan manipulasi koleksi data dengan baik.
- Memahami cara kerja algoritma rekursif dan struktur data fundamental (Stack, Queue, dan Binary Tree) yang menjadi dasar ilmu komputer (*Computer Science*).
- Mengelola data secara persisten pada media penyimpanan melalui operasi *file I/O*.
- Memahami paradigma *Object-Oriented Programming* (OOP) untuk merancang program yang modular, terstruktur, dan mudah dikembangkan.

Selamat belajar dan berlatih!
