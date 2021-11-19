from tkinter import *
import random

# windows utama
ws = Tk()
ws.title('Game Tebak Nomor')
ws.geometry('600x400')
ws.config(bg='#5671A6')

# variable random
ranNum = random.randint(0, 10)
chance = 5
var = IntVar()
disp = StringVar()

# fungsi utama tebak nomor
def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    elif chance <= 0:
        msg = f'You Lost!\nthe right number is {ranNum}'

    disp.set(msg)


# label-label windows
Label(
    ws,
    text='PROGRAM MENEBAK NOMOR ACAK',
    font=('sans-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 18)
).pack()

checkNumber = Button(
    ws,
    text='Masukkan tebakan',
    font=('sans-serif', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))

ws.mainloop()