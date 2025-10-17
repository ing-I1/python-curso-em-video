a = int(input("Type a number: "))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
print(f"{u}, {d}, {c}, {m}")
