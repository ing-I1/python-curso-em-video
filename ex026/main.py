a = str(input("Type your quote: ")).strip().upper()
print(f"{a.count("E")} {a.find("E")+1} {a.rfind("E")+1}")