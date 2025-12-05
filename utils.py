# utils.py

def hitung_rata(nilai):
    """
    Menghitung rata-rata dari list nilai.
    nilai: list berisi 3 nilai angka
    return: float rata-rata
    """
    return sum(nilai) / len(nilai)


def status_lulus(rata, batas=60):
    """
    Menentukan apakah mahasiswa lulus atau tidak.
    rata: nilai rata-rata
    batas: nilai minimum untuk lulus
    """
    return "Lulus" if rata >= batas else "Tidak Lulus"


def cari_tertinggi(data):
    """
    Mengembalikan data mahasiswa dengan rata-rata tertinggi.
    data: list berisi dictionary data mahasiswa
    """
    return max(data, key=lambda x: x["rata"])


def cari_terendah(data):
    """
    Mengembalikan data mahasiswa dengan rata-rata terendah.
    data: list berisi dictionary data mahasiswa
    """
    return min(data, key=lambda x: x["rata"])
