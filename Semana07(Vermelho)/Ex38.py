
estudantes = 0
idadesoma = 0

while estudantes < 15:
    idade = int(input("Digite a sua idade: "))
    idadesoma += idade

    estudantes += 1

media = idadesoma / idade

if media >= 0 and media <= 25:
        print("A turma é considerada jovem.")
elif media >= 26 and media <= 60:
        print("A turma é considerada adulta.")
elif media > 60:
        print("A turma é considerada idosa.")
