import os

fp = r"D:\upb.nama.txt"

def namasaya():
    print("UNIVERSITAS PELITA BANGSA")
    print("Nama: Hendri Rahman")
    print("Kelas: TI.23.B.1")
    print("NIM: 31231036")
    print("=" * 30)

def bacaFile():
    paper = open(fp, "r");
    print("File berisi: \n");
    for i in paper:
        print(i);
    paper.close();

def hurufBesar():
    paper = open(fp, "r+");
    print("Di ubah ke huruf besar: \n")
    for i in paper:
        paper = open(fp, "w")
        upp = i.upper();
        paper.write(upp);
        print(upp);

def deteksiFile():
    if os.path.exists(fp):
        paper = open(fp, "r");
        bacaFile();
        hurufBesar()
        paper.close();
    else:
        paper = open(fp, "w");
        print(f"File {fp} belum ada,  file baru akan dibuat");
        a = input("Masukkan nama anda: ");
        paper.write(a);
        paper.close();
        
def operasi():
    namasaya();
    deteksiFile();
    bacaFile()


operasi()
