def tuliskan_list_nim(3,1,2,3,1,0,3,6,8):
    nim_list = list(str(nim))
    return nim_list

def tampilkan_data_per_index(nim):
    nim_list = tuliskan_list_nim(nim)
    for i in range(len(nim_list)):
        print(f"Index ke-{i}: {nim_list[i]}")

def hitung_rata_rata(nim):
    nim_list = tuliskan_list_nim(nim)
    total = 0
    for num in nim_list:
        if num.isdigit():
            total += int(num)
    rata_rata = total / len(nim_list)
    return rata_rata

# Panggil fungsi untuk menampilkan data per index
nim = 123456500098
tampilkan_data_per_index(nim)

# Panggil fungsi untuk menghitung nilai rata-rata
rata_rata = hitung_rata_rata(nim)
print(f"Rata-rata: {rata_rata}")
