
corredores = 0
somat = 0
abaixo_30 = 0
entre_30e60 = 0

while corredores < 7:
    tempo = float(input("digite o tempo (em minutos): "))
    somat += tempo
    if tempo < 30:
        abaixo_30 += 1
    elif tempo > 30 and tempo < 60:
        entre_30e60 += 1
    corredores += 1

porcentagem_30e60 = (entre_30e60 / corredores) * 100
tempo_m = somat / tempo
print(f"O Tempo médio dos corredores foi: {tempo_m:.2f}")
print("Quantos corredores terminaram em menos de 30 minutos:", abaixo_30)
print(f"A porcentagem de corredores que concluíram entre 30 e 60 minutos foi: {porcentagem_30e60:.2f}%")
