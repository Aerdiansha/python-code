# library grafik dan random untuk digunakan didalam program
from tkinter import *
import random


# player memiliki 3 kesempatan untuk dapat menebak 
# angka random dari 1 sampai 10
kesempatan = 3

# variable dengan nilai acak untuk nanti ditebak oleh player
nomorJawaban = random.randint(1, 10)

def awalAkhir():
    pass

def cekJawaban():
   global kesempatan
   global text

   kesempatan -= 1

   try:
      nomorTebakan = float(kotakJawaban.get())
   except ValueError:
      text.set("Jawaban kamu bukan angka atau tidak mengisi - coba lagi\n kamu punya sisa " + str(kesempatan) +" kesempatan")
      if kesempatan == 0:
          text.set("GAME OVER!\nkamu tidak memberikan jawaban yang benar")
          tombolCek.pack_forget()


   if nomorJawaban == nomorTebakan:
      text.set("Selamat! Kamu menang! \njawaban yang benar = " + str(nomorJawaban))
   elif kesempatan == 0:
      text.set("GAME OVER!\nKamu kehabisan kesempatan menebak \njawaban yang benar = " + str(nomorJawaban))
      tombolCek.pack_forget()
      kotakJawaban.delete(0, END)
   elif nomorTebakan < nomorJawaban:
      text.set(" Jawaban salah - kamu punya sisa " + str(kesempatan) + " kesempatan - \nHINT: Coba nomor lebih tinggi")
      kotakJawaban.delete(0, END)
   elif nomorTebakan > nomorJawaban:
      text.set(" Jawaban salah - kamu punya sisa " + str(kesempatan) + " kesempatan - \nHINT: Coba nomor lebih rendah")
      kotakJawaban.delete(0, END)

# program grafik utama untuk menghasilkan windows
root = Tk() # variable root untuk windows utama
root.title("GAME TEBAK NOMOR") # judul dari programnya
root.geometry("325x250") # lebar dan tinggi dari programnya
root.resizable(False, False)

# text instruksi awalan ketika memulai game
instruksi = Label(root, text="Tebaklah nomor dari 1 sampai 10")
instruksi.pack()

# kotak jawaban untuk player dapat mengisi jawaban angka
kotakJawaban = Entry(root, width=5, borderwidth=4)
kotakJawaban.pack()

# tombol cek untuk membandingkan jawaban player dengan angka acak dari random dengan fungsi utama 
tombolCek = Button(root, text="TEBAK", command=cekJawaban)
tombolCek.pack()

# tombol keluar untuk player dapat menutup program
tombolKeluar = Button(root, text="Keluar", command=root.destroy)
tombolKeluar.pack()

# variable global text untuk dapat menampung string dan menghasilkan text
text = StringVar()
text.set("Kamu punya 3 kesempatan!")

# text untuk mengupdate setiap kali player menjawab salah atau benar 
textUpdate = Label(root, textvariable=text)
textUpdate.pack()

versiGame = Label(root, text="v0.0.1 \ndibuat oleh kelompok 1")
versiGame.pack(pady=20)

# program akhiran dari grafis utama windows
root.mainloop()
