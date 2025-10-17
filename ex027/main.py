a = str(input("Type a name: ")).strip().title()
b = a.split()
print(f"{b[0]} {b[len(b)-1]}")