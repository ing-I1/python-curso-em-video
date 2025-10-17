import random
n = [1, 2, 3, 4, 5]
nr = random.choice(n)
a = str(input("Pick a number between 1 and 5: "))
if a == nr:
    print(f"The number was {nr} You win")
else:
    print(f"The number was {nr} You lose")
    