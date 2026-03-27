
pontuaçao1 = int(input("Qual foi a pontuação do time azul? "))
pontuaçao2 = int(input("Qual foi a pontuação do time vermelho? "))

if pontuaçao1 > pontuaçao2:
    print("Time azul venceu e o Time vermelho perdeu.")
elif pontuaçao2 > pontuaçao1:
    print("Time vermelho venceu e o Time azul perdeu.")
else:
    print("Houve um empate.")
