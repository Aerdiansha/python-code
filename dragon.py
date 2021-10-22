import random
import time

# Fungsi intro cerita
# def Fungsi tidak akan tampil apabila tidak dipanggil 
# dan hanya akan disimpan terlebih dahulu di awal baris kode
def displayIntro():
    print("You are on a planet full of dragon. In front of you,")
    time.sleep(3)
    print("You see two caves. In one cave, the dragon is friendly")
    time.sleep(3)
    print("and will share his treasure with you. The other dragon")
    time.sleep(3)
    print("is greedy and hungry, and will eat you on sight.")
    print()

# Fungsi pemilihan cave
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

# Fungsi cerita lanjutan setelah player memilih
def checkCave(chooseCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)

    # Variable random untuk menentukan nasib player ketika memilih cave
    friendlyCave = random.randint(1, 2)

    # If-else pemilihan cave
    if chooseCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bites!")

# operator utama while untuk menanyakan player bermain lagi
# ini adalah permulaan baris game kita
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":

        displayIntro()

        caveNumber = chooseCave()

        checkCave(caveNumber)

        print("Do you want to play again? (yes or no)")
        playAgain = input()