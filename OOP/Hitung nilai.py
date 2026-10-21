# Menghitung nilai akhir berdasarkan bobot.
def hitung_nilai_akhir(tugas, uts, uas):
    nilai = (
        0.30 * tugas +
        0.30 * uts +
        0.40 * uas
    )
    return nilai
# Menghitung nilai dari contoh data.
hasil = hitung_nilai_akhir(80, 75, 85)
print("Nilai akhir:", hasil)
