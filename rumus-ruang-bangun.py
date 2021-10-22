garis = "===================================================="

print("1. Rumus menghitung volume Kubus")
s1 = int(input("Masukkan Nilai sisi 1: "))
s2 = int(input("Masukkan Nilai sisi 2: "))
s3 = int(input("Masukkan Nilai sisi 3: "))
vk = s1 * s2 * s3
print("Volume Kubus = ", s1, "X", s2, "X", s3, "= %.0f" %vk)
print(garis)

print("2. Rumus menghitung volume Balok")
p1 = int(input("Masukkan nilai panjang: "))
l1 = int(input("Masukkan nilai Lebar: "))
t1 = int(input("Masukkan nilai Tinggi: "))
vb = p1 * l1 * t1
print("Volume Balok = ", p1, "X", l1, "X", t1, "= %.0f" %vb)
print(garis)

print("3. Rumus menghitung volume tabung")
pi = 3.14
print("Nilai pi = ", pi)
r2 = int(input("masukkan nilai jari-jari(akar pangkat): ")) **2
t2 = int(input("masukkan nilai tinggi: "))
vt = (pi * r2) * t2
print("Volume tabung = ", pi, "X", r2, "X", t2, "= %.0f"%vt)
print(garis)

print("4. Rumus menghitung volume limas segi-empat")
p3 = int(input("Masukkan nilai panjang: "))
l3 = int(input("Masukkan nilai lebar: "))
t3 = int(input("Masukkan nilai tinggi: "))
vl = 1/3 * (p3 * l3) * t3
print("Volume limas = 1/3 X Luas alas X Tinggi")
print("Volume limas = ", "1/3 X (", p3, "X", l3, ") X", t3, "= %.0f" %vl)
print(garis)