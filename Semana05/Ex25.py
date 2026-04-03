
print("Você está preparado para participar da Corrida Anual dos Campões?")
print("Responda as seguintes perguntas:")

print("\nVocê treinou regularmente nas últimas semanas?")
r1 = input("Digite a sua resposta: ").upper()
print("Participou de treinos longos (acima de 10 km)?")
r2 = input("Digite a sua resposta: ").upper()
print("Seguiu uma dieta especial para a corrida?")
r3 = input("Digite a sua resposta: ").upper()
print("Já competiu em provas oficiais neste ano?")
r4 = input("Digite a sua resposta: ").upper()
print("Conta com acompanhamento de treinador ou equipe?")
r5 = input("Digite a sua resposta: ").upper()

resultado = 0
if r1 == "SIM":
    resultado += 1
if r2 == "SIM":
    resultado += 1
if r3 == "SIM":
    resultado += 1
if r4 == "SIM":
    resultado += 1
if r5 == "SIM":
    resultado += 1

if resultado == 5:
    print("Atleta de Elite (pronto para o pódio!)")
elif resultado >= 3:
    print("Atleta Competitivo (tem boas chances de se destacar)")
elif resultado == 2:
    print("Participante Casual (ainda precisa de mais treino)")
else:
    print("Não Preparado (talvez seja melhor assistir da arquibancada este ano)")
