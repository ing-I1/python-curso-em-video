a = float(input("Read the car speed in km/h: "))
if(a > 80):
    print(f"You get finned by R$ {(a-80)*7}")
else:
    print("You good to go")