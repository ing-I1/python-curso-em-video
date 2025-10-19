a = float(input("Type a distance in KM: "))
if(a<=200):
    print(f"Your price is: {a*0.5}")
else:
    print(f"Your price is: {a*0.45}")