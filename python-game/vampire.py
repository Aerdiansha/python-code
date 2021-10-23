name = input("who are you: ")
age = int(input("what your age: "))

print("hello " + name)
if age < 12:
    print("you are a child")
elif age > 200:
    print("Are you immortal!?")
elif age > 100:
    print("who are you!?")