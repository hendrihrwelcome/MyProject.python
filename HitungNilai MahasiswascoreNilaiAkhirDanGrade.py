def nama():
    print("UNIVERSITAS PELITA BANGSA")
    print("UAS SEMESTER GASAL TAHUN AJARAN 2023/2024")
    print("Dosen: Sophian Andika Sardi, SKom., MKom.")
    print("=========================================")
    print("Nama: Hendri Rahman")
    print("Kelas: TI.23.B.1")
    print("NIM: 312310368")

def input_nilai(prompt):
    return float(input(prompt))

def hitung_nilai_akhir(nilai_tugas, nilai_absen, nilai_uts, nilai_uas):
    persentase_tugas = 0.15
    persentase_absen = 0.05
    persentase_uts = 0.35
    persentase_uas = 0.45
    return (nilai_tugas * persentase_tugas) + (nilai_absen * persentase_absen) + (nilai_uts * persentase_uts) + (nilai_uas * persentase_uas)

def hitung_grade(nilai_akhir):
    if nilai_akhir >= 90:
        return 'A'
    elif nilai_akhir >= 85:
        return 'B+'
    elif nilai_akhir >= 80:
        return 'B'
    elif nilai_akhir >= 70:
        return 'C+'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    elif nilai_akhir < 50:
        return 'E'

def main():
    nama()
    nilai_tugas = input_nilai("Masukkan nilai tugas: ")
    nilai_absen = input_nilai("Masukkan nilai absen: ")
    nilai_uts = input_nilai("Masukkan nilai UTS: ")
    nilai_uas = input_nilai("Masukkan nilai UAS: ")

    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_absen, nilai_uts, nilai_uas)

    print("\nNilai Akhir: {:.2f}".format(nilai_akhir))
    print("Grade: {}".format(hitung_grade(nilai_akhir)))

if __name__ == "__main__":
    main()