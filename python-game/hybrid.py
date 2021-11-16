# import turtle

# pen = turtle.Turtle()
# pen.speed(0)
# pen.hideturtle()

# #Creating Menu option buttons
# def button(length):
#     for i in range(4):
#         pen.forward(length)
#         pen.left(90)

# def column(n, length):
#     pen.left(270)
#     for i in range(n):
#         button(length)
#         pen.forward(length)
#     pen.penup()
#     pen.left(90)
#     pen.forward(n * length)
#     pen.left(180)
#     pen.pendown()

# column(5, 100)

# #Menu Options
# pen.penup()
# pen.goto(8, -46)
# pen.write("START GAME!", font=("Arial",12,"normal"))

# pen.penup()
# pen.goto(6, -145)
# pen.write("RULES", font=("Arial",12,"normal"))

# pen.penup()
# pen.goto(3, -248)
# pen.write("HIGH SCORE", font=("Arial",12,"normal"))

# pen.penup()
# pen.goto(4, -343)
# pen.write("FAQ", font=("Arial",12,"normal"))

# pen.penup()
# pen.goto(3, -450)
# pen.write("QUIT GAME", font=("Arial",12,"normal"))

# #Making options clickable
# def btnclick(x,y):
#     if x > 0 and x < 101 and y > 0 and y < -101:
#         print("Start Game")
#         print(x, y)
#         turtle.clearscreen()
#     elif x > 0 and x < 101 and y > 101 and y < -201:
#         print("Rules")
#         print(x, y)
#         turtle.clearscreen()
#     elif x > 0 and x < 101 and y > 201 and y < -301:
#         print("Highscore")
#         print(x, y)
#         turtle.clearscreen()
#     elif x > 0 and x < 101 and y > 301 and y < -401:
#         print("Hi")
#         print(x, y)
#         turtle.clearscreen()
#     elif x > 0 and x < 101 and y > 401 and y < -501:
#         print("Hi")
#         print(x, y)
#         turtle.clearscreen()
#     elif x > 0 and x < 101 and y > 501 and y < -601:
#         print("Hi")
#         print(x, y)
#         turtle.clearscreen()
#     else:
#         print("Click One Of The Options!")
#         print(x, y)
#         btnclick(x, y)

# turtle.onscreenclick(btnclick, 1)
# turtle.listen()

# turtle.done()

import turtle
def triangle():
    for i in range(3):
        turtle.forward(50)
        turtle.right(360/3)


def square():
    for i in range(4):
        turtle.forward(50)
        turtle.right(360/4)

def pentagon():
    for i in range(5):
        turtle.forward(50)
        turtle.right(360/5)

turtle.shape('turtle')
answer = input('pick a shape.. triangle, square or pentagon: ')

print(answer)

if answer ==('triangle'):
    triangle()

elif answer == ('square'):
    square()

elif answer == ('pentagon'):
    pentagon()

else:
    print ('wrong input')
