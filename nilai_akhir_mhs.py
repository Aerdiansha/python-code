# persiapan variable nilai
absen = float(input("Masukkan nilai absensi: "))
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# garis - garis
gr = '========================================'

# perhitungan nilai akhir
nilaiAkhir = (absen*0.1)+(tugas*0.15)+(uts*0.35)+(uas*0.5)

# operasi perhitungan grade
if nilaiAkhir >= 80:
    index = 'A'
elif nilaiAkhir >= 70:
    index = 'B'
elif nilaiAkhir >= 55:
    index = 'C'
elif nilaiAkhir >= 40:
    index = 'D'
elif nilaiAkhir >= 0:
    index = 'E'
else:
    print("Tidak punya nilai")

# hasil
print("\n"+gr)
print("Nilai akhir = ", nilaiAkhir)
print("Grade : ", index)
print(gr)
