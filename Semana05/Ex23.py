
f1 = float(input("Digite a força 1: "))
f2 = float(input("Digite a força 2: "))
f3 = float(input("Digite a força 3: "))

equilibrio1 = (f1 + f2) > f3
equilibrio2 = (f2 + f3) > f1
equilibrio3 = (f3 + f1) > f2

if equilibrio1 or equilibrio2 or equilibrio3:
    if f1 == f2 == f3:
        print("Equilibrio positivo.")
        print("Simétrico.")
    elif f1 == f2 or f1 == f3 or f2 == f3:
        print("Equilibrio positivo.")
        print("Parcialmente simétrico.")
    else:
        print("Equilibrio positivo.")
        print("Assimétrico")
else:
    print("Não há equilibrio.")
