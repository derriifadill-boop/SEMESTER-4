"""
Modul Kalkulator Nilai Mahasiswa
Menghitung nilai akhir berdasarkan komponen: tugas, kuis, UTS, UAS.
"""

BOBOT_TUGAS = 0.20
BOBOT_KUIS  = 0.30
BOBOT_UTS   = 0.20
BOBOT_UAS   = 0.30

BATAS_GRADE = [
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
]
GRADE_DEFAULT = "E"


def hitung_nilai_akhir(tugas: float, kuis: float, uts: float, uas: float) -> float:
    """Menghitung nilai akhir berbobot dari empat komponen penilaian."""
    return (
        tugas * BOBOT_TUGAS
        + kuis  * BOBOT_KUIS
        + uts   * BOBOT_UTS
        + uas   * BOBOT_UAS
    )


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade huruf berdasarkan nilai akhir."""
    for batas, grade in BATAS_GRADE:
        if nilai_akhir >= batas:
            return grade
    return GRADE_DEFAULT


def tampilkan_hasil_mahasiswa(nama: str, nilai_akhir: float, grade: str) -> None:
    """Menampilkan hasil penilaian satu mahasiswa ke konsol."""
    print(f"Nama  : {nama}")
    print(f"Nilai : {nilai_akhir:.2f}")
    print(f"Grade : {grade}")
    print("-" * 30)


def proses_seluruh_mahasiswa(data_mahasiswa: list[dict]) -> list[float]:
    """
    Memproses seluruh data mahasiswa, menampilkan hasil tiap mahasiswa,
    dan mengembalikan daftar nilai akhir untuk keperluan statistik.
    """
    daftar_nilai_akhir = []

    for mahasiswa in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["kuis"],
            mahasiswa["uts"],
            mahasiswa["uas"],
        )
        grade = tentukan_grade(nilai_akhir)
        tampilkan_hasil_mahasiswa(mahasiswa["nama"], nilai_akhir, grade)
        daftar_nilai_akhir.append(nilai_akhir)

    return daftar_nilai_akhir


def hitung_rata_rata_kelas(daftar_nilai: list[float]) -> float:
    """Menghitung rata-rata nilai seluruh mahasiswa dalam satu kelas."""
    if not daftar_nilai:
        return 0.0
    return sum(daftar_nilai) / len(daftar_nilai)


def main():
    data_mahasiswa = [
        {"nama": "Robi",   "tugas": 80, "kuis": 75, "uts": 90, "uas": 85},
        {"nama": "Ganjaro",    "tugas": 60, "kuis": 55, "uts": 70, "uas": 65},
        {"nama": "Ben", "tugas": 90, "kuis": 95, "uts": 88, "uas": 92},
        {"nama": "Deri",   "tugas": 45, "kuis": 50, "uts": 40, "uas": 48},
    ]

    print("=" * 30)
    print("   HASIL NILAI MAHASISWA")
    print("=" * 30)

    daftar_nilai_akhir = proses_seluruh_mahasiswa(data_mahasiswa)

    rata_rata = hitung_rata_rata_kelas(daftar_nilai_akhir)
    print(f"Rata-rata kelas : {rata_rata:.2f}")


if __name__ == "__main__":
    main()