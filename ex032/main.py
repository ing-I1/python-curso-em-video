from datetime import date
a = int(input("Time your year"))
if a == 0:
    a = date.today().year()
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f"The year {a} is BISSEXTO")
else:
    print(f"The year {a} isn't BISSEXTO")