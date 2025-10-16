import random
a = str(input("Type a student name: "))
b = str(input("Type a 2nd student name: "))
c = str(input("Type a 3rd student name: "))
list = [a, b, c]
print(f"The student choiced was: {random.choice(list)}")