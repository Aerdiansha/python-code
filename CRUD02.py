nim = []
nama = []
asal = []

pilihan = 1
while pilihan != 0:
    print("1. Input data")
    print("2. Tampilan data")
    print("3. Hapus data")
    print("0. EXIT")

    pilihan = int(input("Masukkan Pilihan: "))

    if pilihan == 1:
        Nim = input("Masukkan NIM: ")
        nim.append(Nim)
        Nama = input("Masukkan Nama: ")
        nama.append(Nama)
        Asalan = input("Masukkan tempat asal: ")
        asal.append(Asalan)
    elif pilihan == 2:
        penentu = True
        for i in range(len(nim)):
            if penentu:
                print('nim\tnama\tasal')
            print(nim[i]+'\t'+nama[i]+'\t'+asal[i])
            penentu = False
    elif pilihan == 3:
        Nim = input("Masukkan Nim: ")
        for i in range(len(nim)):
            if Nim == nim[i]:
                print(i)
                del nim[i]
                del nama[i]
                del asal[i]
                break
