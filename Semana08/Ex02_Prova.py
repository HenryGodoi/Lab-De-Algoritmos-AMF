
dia = int(input()) # código reformulado

while dia <= 365 and dia >= 1: 
    # dia = int(input()) (código errado)
    # notei um erro no código, o "dia = int(input())" estava dentro do while e por isso o código não funcionava
    if dia >= 1 and dia <= 59:
        print()
    elif dia > 59 and dia <= 120:
        print()
    elif dia > 120 and dia <= 181:
        print()
    elif dia > 181 and dia <= 243:
        print()
    elif dia > 243 and dia <= 304:
        print()
    elif dia > 304 and dia <= 265:
        print()
    else:
        print()
