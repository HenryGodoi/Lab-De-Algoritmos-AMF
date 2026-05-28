
def converte(hora, minuto):    
    hora12 = hora - 12
    print(f"{hora12}:{minuto} P.M")

def main():
    hora = int(input("Digite a hora(0 a 23): "))
    minuto = int(input("Digite o minuto(0 a 59): "))
    
    if hora > 12:
        converte(hora, minuto)
    else:
        print(f"{hora}:{minuto} P.M")

main()
