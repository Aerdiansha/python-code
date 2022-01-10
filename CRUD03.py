idkry = []
nmkry = []
jabat = []
gaji = []
tunja = []

g = '=============================='

pilihan = 1
while True:
    print("1. Input Data Karyawan")
    print("2. Lihat Data Karyawan")
    print("3. Hapus Data karyawan")
    print("0. QUIT")
    print(g)

    pilihan = int(input("Masukkan Pilihan: "))

    if pilihan == 1:
        print(g)
        intID = input("Masukkan ID Karyawa: ")
        idkry.append(intID)
        nama = input("Masukkan Nama Karyawan: ")
        nmkry.append(nama)
        jabatan = input("Masukkan Jabatan: ")
        jabat.append(jabatan)
        gajihan = input("Masukkan Gaji: ")
        gaji.append(gajihan)
        tunjangan = input("Masukkan Tunjangan: ")
        tunja.append(tunjangan)
        print(g+"\n")

    elif pilihan == 2:
        penentu = True
        for i in range(len(idkry)):
            if penentu:
                print(g)
                print('ID\tNama\tJabatan\t Gaji\tTunjangan')
                print(g)
            print(idkry[i]+'\t'+nmkry[i]+'\t'+jabat[i],'\t ',gaji[i],'\t',tunja[i])
            print(g)
            penentu = False
    elif pilihan == 3:
        intID = input("Masukkan ID: ")
        for i in range(len(idkry)):
            if intID == idkry[i]:
                print(i)
                del idkry[i]
                del nmkry[i]
                del jabat[i]
                del gaji[i]
                del tunja[i]
    elif pilihan == 0:
        break