def nama():
    print("UNIVERSITAS PELITA BANGSA")
    print("Nama: Hendri Rahman")
    print("Kelas: TI.23.B.1")
    print("NIM: 312310368")
    print("=" * 30)

def inputNilaiTugas(a):
    nilai = float(a)
    nilai *= 0.15
    print("Nilai Tugas adalah: %", nilai)
    return nilai

def inputNilaiAbsen(a):
    nilai = float(a)
    nilai *= 0.05
    print("Nilai Absen adalah: %", nilai )
    return nilai

def inputNilaiUTS(a):
    nilai = float(a)
    nilai *= 0.35
    print("Nilai UTS adalah: %", nilai)
    return nilai

def inputNilaiUAS(a):
    nilai = float(a)
    nilai *= 0.45
    print("Nilai UAS adalah: %", nilai) 
    return nilai

def operasi():
    nama()
    hasil = 0
    nama_siswa = input("Masukkan Nama siswa: ")
    nilai_tugas = input("Masukkan Nilai Tugas: ")
    nilai_absen = input("Masukkan Nilai Absen: ")
    nilai_uts = input("Masukkan Nilai UTS: ")
    nilai_uas = input("Masukkan Nilai UAS: ")
    print("=" * 30)
    print("Nilai dari siswa: ", nama_siswa)
    hasil += inputNilaiTugas(nilai_tugas)
    hasil += inputNilaiAbsen(nilai_absen)
    hasil += inputNilaiUTS(nilai_uts)
    hasil += inputNilaiUAS(nilai_uas)
    print("Total Nilai adalah: %", hasil)

# Panggil fungsi operasi
operasi()
