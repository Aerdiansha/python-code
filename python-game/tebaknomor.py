# program menebak angka Random
import random # melakukan import module random ke dalam program

kesempatan = 0 # Variable kesempatan dengan nilai 0 (nol)

print("\t\tSELAMAT DATANG DI PROGRAM TEBAK NOMOR \n")
print("Silahkan masukkan nama : ")
nama = input() # inputan nama dari user

number = random.randint(1, 10) # variable number dengan nilai module random.randint(param1, param2)

print("Saya sedang memikirkan sebuah angka dari 1 sampai 10, bisakah " + nama + " menebak")

# Program while loops untuk menebak angka dari user
while kesempatan < 6: # kesempatan sebanyak 5 kali
    print("Coba tebak: ")
    tebak = input()     # menginput nilai dari user untuk menebak angka
    tebak = int(tebak)  # mengubah nilai string ke integer dari inputan user
 
    kesempatan = kesempatan + 1 # varible kesempatan bertambah ketika user mencoba menebak

    # statement if menebak number
    if tebak < number:
        print("Tebakanmu terlalu kecil, Coba lagi")

    if tebak > number:
        print("Tebakanmu terlalu besar, Coba lagi")
    
    if tebak == number:
        break

if tebak == number:
    kesempatan = str(kesempatan)
    print("Selamat " + nama + "kamu berhasil menebaknya dengan " + kesempatan + " kali.")

if tebak != number:
    number = str(number)
    print("Nilai yang saya maksud adalah " + number)

