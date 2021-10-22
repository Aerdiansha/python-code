import random
# variable
number1 = random.randint(1,10)
number2 = random.randint(1,10)

# question
print('what is ' + str(number1) + '+' + str(number2) + '?')

# variable for user to answer
answer = input()

# condition operation
if answer == number1 + number2:
    print("Correct")
else:
    print("Nope! the answer is "  + str(number1 + number2))