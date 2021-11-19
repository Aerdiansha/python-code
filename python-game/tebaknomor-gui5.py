# Imports
from tkinter import *
from tkinter import messagebox
from random import randint



# Screen
root = Tk()
root.geometry("500x500")
root.title("Number Guessing Game")

# attempts = 10


# Generate Number Function
def GenerateNumberFunc():
    global Number
    # Generate Number
    Number = randint(1, 10)
    
    # MessageBox to show that a number was generated
    messagebox.showinfo("A Number was Generated!", "Please Guess the Number")



# Guess Number Function
def GuessNumberFunc():
    global Number
    # global attempts

    # attempts -= 1
    # Get Value from Answer Entry Box
    UserResponse = AnswerEntry.get()
    
    # Convert Value from Answer Entry Box to a Number
    UserResponse = int(UserResponse)

    # Check if the User Response was higher, lower, or equal to the correct number
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect! Please Guess Lower", fg="Red")
    # elif attempts == 0:
    #     ResultLabel.config(text="You are out of attempts")
    #     GuessBtn.place_forget()
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect! Please Guess Higher", fg="Red")
    else:
        ResultLabel.config(text="You Guess Correctly! The Number was {}".format(Number), fg="Green")
        AnswerEntry.delete(0, "end")



# Title
Title = Label(root, text="Number Guessing Game", font=("Arial", 30))
Title.pack()



# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=60)



# Guess the Number Label
GuessNumLabel = Label(MainFrame, text="Guess a number from 1 to 10:", font=("Arial", 20))
GuessNumLabel.pack()



# Answer Entry
AnswerEntry = Entry(MainFrame, font=("Arial", 16))
AnswerEntry.pack(pady=10)



# Generate Number Button
GenerateNumberBtn = Button(MainFrame, text="Generate Number", width=16, font=("Arial", 16), background="Dodgerblue", command=GenerateNumberFunc)
GenerateNumberBtn.pack()



# Guess Button
GuessBtn = Button(MainFrame, text="Guess", width=16, font=("Arial", 16), background="#15e650", command=GuessNumberFunc)
GuessBtn.pack(pady=5)



# Result Label
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()



# Mainloop
root.mainloop()