# Program menghitung nilai Mahasiswa
nama = input("Nama Anda : ")
nilai = int(input("Nilai Anda : "))

if nilai >= 80:
    print("Nilai : A")
elif nilai > 60:
    print("Nilai : B")
elif nilai <= 60:
    print("Nilai : C")