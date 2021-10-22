# Program aplikasi kalkulasi gaji karyawan
# persiapan
gr1 = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
gr2 = '|===================================|'
gr3 = '|-----------------------------------|'

# outputan
print(gr1)
print("PROGRAM KALKULASI GAJI KARYAWAN")
print(gr1)
print("")
print("1. direktur")
print("2. manager")
print("3. karyawan")
print("4. Office boy")
print("5. exit")
print("")
print(gr1)
pilih = int(input("Masukkan pilihan anda : "))
print(gr1)

# Decision operator
if pilih == 1:
    print('')
    print("\tkalkulasi gaji direktur")
    gaji = 3000000
    tunjangan = 0.25*gaji
    PPN = 0.1*gaji
    total = (gaji+tunjangan)-PPN
    print(gr2)
    print("|gaji pokok = ",gaji)
    print("|Tunjangan = ", tunjangan)
    print("|pajak penghasilan = ", PPN)
    print(gr2)
    print("Total gaji direktur Rp.", total)
    print("")
elif pilih == 2:
    print('')
    print("\tkalkulasi gaji manager")
    gaji = 2000000
    tunjangan = 0.125*gaji
    PPN = 0.1*gaji
    total = (gaji+tunjangan)-PPN
    print(gr2)
    print("|gaji pokok = ",gaji)
    print("|Tunjangan = ", tunjangan)
    print("|pajak penghasilan = ", PPN)
    print(gr2)
    print("Total gaji manager Rp.", total)
    print("")
elif pilih == 3:
    print('')
    print("\tkalkulasi gaji karyawan")
    gaji = 1000000
    tunjangan = 0.6*gaji
    PPN = 0.1*gaji
    total = (gaji+tunjangan)-PPN
    print(gr2)
    print("|gaji pokok = ",gaji)
    print("|Tunjangan = ", tunjangan)
    print("|pajak penghasilan = ", PPN)
    print(gr2)
    print("Total gaji karyawan Rp.", total)
    print("")
elif pilih == 4:
    print('')
    print("\tkalkulasi gaji Office boy")
    gaji = 800000
    tunjangan = 0.16*gaji
    PPN = 0.1*gaji
    total = (gaji+tunjangan)-PPN
    print(gr2)
    print("|gaji pokok = ",gaji)
    print("|Tunjangan = ", tunjangan)
    print("|pajak penghasilan = ", PPN)
    print(gr2)
    print("Total gaji Office Boy Rp.", total)
    print("")
elif pilih == 5:
    print("Terima kasih telah menggunakan program kalkulasi gaji!")
else:
    print("Nomor yang anda inputkan salah! Coba lagi")
