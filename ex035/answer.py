a = float(input("Insert A: "))
b = float(input("Insert B: "))
c = float(input("Insert C: "))
if a < b + c and b < a + c and c < a + b:
    print("A triangle can be formed")
else:
    print("A triangle can't be formed")