# Meminta masukkan NIM
nim_list = ['3','1','2','3','1','0','3','6','8']
for i in range(5):
    nim = input(f"Masukkan NIM ke-{i+1}: ")
    nim_list.append(nim)

# Menampilkan indeks ke-4 (elemen ke-5 dalam list)
print(f"Indeks ke-4: {nim_list[3]}")

# Menampilkan indeks ke-2 sampai terakhir
print(f"Indeks ke-2 sampai terakhir: {nim_list[1:]}")

# Menampilkan indeks terakhir
print(f"Indeks terakhir: {nim_list[-1]}")

# Mengubah indeks ke-4 menjadi 0
nim_list[3] = '0'

# Menampilkan hasil setelah perubahan
print("List setelah mengubah indeks ke-4 menjadi 0:", nim_list)