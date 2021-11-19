# module/library
import tkinter as tk
import random

# Windows utama
root = tk.Tk()
root.title("Game")
root.geometry('600x400')
root.config(bg='#065569')
root.resizable(width=False, height=True)

# variabel
kesempatan = 10
hint = StringVar()



# Fungsi - fungsi
def NumGuessGame():
    global Number



# widget-widget
title = tk.Label(root,
                 text="Selamat Datang di Game Tebak Nomor",
                 font=("Times New Roman",24),
                 fg="#ffffff",
                 bg="#065569",
                 padx=10,
                 pady=0,
                 )

jawabanEntry = tk.Entry(root,
                        font=("Times New Roman,", 12),
                        )
tombolJawaban = tk.Button(root,
                          font=("Times New Roman,", 12),
                          text="Tebak!",
                          padx=0,
                          pady=0,
                          command=NumGuessGame())

# posisi widget
title.pack()
jawabanEntry.place(x=200, y=55)
tombolJawaban.place(x=390,y=55)

# Akhiran windows
root.mainloop()


