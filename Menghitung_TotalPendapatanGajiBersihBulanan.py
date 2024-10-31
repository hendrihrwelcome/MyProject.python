def hitung_pendapatan(gaji_pokok, jumlah_anak, masuk_kerja_hari):
    # Menghitung tunjangan istri/suami
    tunjangan_istri_suami = 0.1 * gaji_pokok

    # Menghitung tunjangan anak
    tunjangan_anak = 0.05 * gaji_pokok * jumlah_anak

    # Menghitung total tunjangan
    total_tunjangan = tunjangan_istri_suami + tunjangan_anak

    # Menghitung pajak
    pajak = 0.15 * (gaji_pokok + total_tunjangan)

    # Menghitung bantuan transport
    bantuan_transport = 20000 * masuk_kerja_hari

    # Menghitung BPJS
    bpjs = 75000

    # Menghitung take home pay
    take_home_pay = gaji_pokok + total_tunjangan - pajak + bantuan_transport - bpjs

    # Mengembalikan nilai tunjangan istri, tunjangan anak, uang transport, pajak, dan take home pay
    return tunjangan_istri_suami, tunjangan_anak, total_tunjangan, pajak, bantuan_transport, bpjs, take_home_pay

# Deklarasi nama dan keterangan tugas
print("UNIVERSITAS PELITA BANGSA")
print("Tugas Pertemuan - 12")
print("# Menghitung Total Pendapatan Gaji Bersih Bulanan #")
print("Bahasa Pemrograman Python")
print("Dosen: Sophian Andhika Sardi, S.Kom., M.Kom.")
print("==================================================")
print("Nama : Hendri Rahman")
print("NIM  : 312310368")
print("Kelas: Ti.23.B.1")
print("==================================================")

# Input dari pengguna
gaji_pokok = float(input("Masukkan gaji pokok: "))
jumlah_anak = int(input("Masukkan jumlah anak: "))
masuk_kerja_hari = int(input("Masukkan jumlah hari masuk kerja dalam sebulan: "))

# Memanggil fungsi untuk menghitung pendapatan
tunjangan_istri, tunjangan_anak, total_tunjangan, pajak, bantuan_transport, bpjs, hasil_pendapatan = hitung_pendapatan(gaji_pokok, jumlah_anak, masuk_kerja_hari)

# Menampilkan hasil
print("\nRincian Pendapatan Bulanan:")
print(f"Gaji Pokok: Rp {gaji_pokok:.2f}")
print(f"Tunjangan Istri/Suami: Rp {tunjangan_istri:.2f}")
print(f"Tunjangan Anak: Rp {tunjangan_anak:.2f}")
print(f"Total Tunjangan: Rp {total_tunjangan:.2f}")
print(f"Pajak: Rp {pajak:.2f}")
print(f"Bantuan Transport: Rp {bantuan_transport:.2f}")
print(f"Potongan BPJS: Rp {bpjs:.2f}")
print(f"Take Home Pay/Gaji Bersih Adalah: Rp {hasil_pendapatan:.2f}")
