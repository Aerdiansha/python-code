import random

print("I will flip a coin 1000 times. Guess how many times it will comes up heads. (Enter to begin)")
input()
flips = 0
heads = 0

while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 flips and there have been ' + str(heads) + " heads.")
    if flips == 100:
        print("At 100 tosses, heads has come up " + str(heads) + " times so far.")
    if flips == 500:
        print("Half way done, and heads has come up " +str(heads) + " times")

print()
print("out of 1000 times coin tosses, heads came up " + str(heads) + " times!")
print("were you close?")