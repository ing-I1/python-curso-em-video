import random
a = str(input("Type a student name: "))
b = str(input("Type a 2nd student name: "))
c = str(input("Type a 3rd student name: "))
ls = [a, b, c]
random.shuffle(ls)
print(f"The student order is: {ls}")