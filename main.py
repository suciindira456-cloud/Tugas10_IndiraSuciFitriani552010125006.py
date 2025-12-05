# main.py
from utils import hitung_rata, status_lulus, cari_tertinggi, cari_terendah

print("=== SISTEM NILAI MODULAR ===")

data_mhs = []

jumlah = int(input("Berapa mahasiswa? "))

# Input data mahasiswa
for i in range(jumlah):
    print(f"\nData mahasiswa ke-{i+1}")
    nama = input("Nama : ")
    n1 = float(input("Nilai 1 : "))
    n2 = float(input("Nilai 2 : "))
    n3 = float(input("Nilai 3 : "))

    nilai = [n1, n2, n3]
    rata = hitung_rata(nilai)
    status = status_lulus(rata)

    # Simpan ke list
    data_mhs.append({
        "nama": nama,
        "nilai": nilai,
        "rata": rata,
        "status": status
    })

# Tampilkan hasil
print("\n=== REKAP NILAI ===")
for m in data_mhs:
    print(f"{m['nama']} - Rata-rata: {m['rata']:.2f} - {m['status']}")

# Cari tertinggi & terendah
tertinggi = cari_tertinggi(data_mhs)
terendah = cari_terendah(data_mhs)

print("\nMahasiswa Nilai Tertinggi:")
print(f"{tertinggi['nama']} - {tertinggi['rata']:.2f}")

print("\nMahasiswa Nilai Terendah:")
print(f"{terendah['nama']} - {terendah['rata']:.2f}")
