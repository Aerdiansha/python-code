nilai1, nilai2 = 0, 1
hitungan = 0

print("PROGRAM URUTAN ANGKA FIBONACCI")
print("")
while True:
   angka = int(input("Berapa banyak angka yang mau ditampilkan?"))
   if angka <= 0:
      print("angka harus positif")
   while hitungan < angka:
      print(nilai1)
      nilain = nilai1 + nilai2
      nilai1 = nilai2
      nilai2 = nilain
      hitungan += 1