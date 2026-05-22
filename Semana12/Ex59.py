
def lernotas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    return n1, n2

def calcularmedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

def situacao(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    
def main():
    nota1, nota2 = lernotas()
    media = calcularmedia(nota1, nota2)
    situacao(media)

main()
