
import random

oliveiras = random.randint(1, 100)
escolha = 0

while escolha != oliveiras:
    escolha = int(input("Digite um número: "))

    if escolha < oliveiras:
        print("Há mais oliveiras, tente um número maior.")
    elif escolha > oliveiras:
        print("Há menos oliveiras, tente um número menor.")
    elif escolha == oliveiras:
        print("Parabéns! Você descobriu a quantidade de oliveiras!")
    
