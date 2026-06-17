
import datetime
import matplotlib.pyplot as plt

CAPACIDADE_MAXIMA = 5
CAPACIDADE_ESPERA = 1
VALOR_DIARIA_CURTA = 127.00  
VALOR_DIARIA_LONGA = 115.00   
LIMITE_DIAS_DIARIA = 30

codigos_estacionamento = []    
horarios_entrada = []           

codigo_espera = []               
horario_espera = []              

total_estacionamentos_sucesso = 0
total_retiradas = 0
valor_em_caixa = 0.0

tempo_atual = None 


def obter_tempo_inicial():
    momento = datetime.datetime.now()
    return momento


def adiantar_tempo_em_dias(momento_atual, quantidade_dias):
    novo_momento = momento_atual + datetime.timedelta(days=quantidade_dias)
    return novo_momento


def adiantar_tempo_em_meses(momento_atual, quantidade_meses):
    dias_equivalentes = quantidade_meses * 30
    novo_momento = adiantar_tempo_em_dias(momento_atual, dias_equivalentes)
    return novo_momento


def calcular_dias_estacionado(momento_entrada, momento_saida):
    diferenca = momento_saida - momento_entrada
    dias = diferenca.days

    contador_dias = 0
    if dias < 1:
        contador_dias = 1
    else:
        contador_dias = dias

    return contador_dias


def contar_vagas_ocupadas():
    contador = 0
    for i in range(len(codigos_estacionamento)):
        contador = contador + 1
    return contador


def existe_vaga_livre():
    ocupadas = contar_vagas_ocupadas()

    contador_disponivel = 0
    if ocupadas < CAPACIDADE_MAXIMA:
        contador_disponivel = 1

    return contador_disponivel


def existe_aeronave_na_espera():
    contador_espera = 0
    for i in range(len(codigo_espera)):
        contador_espera = contador_espera + 1
    return contador_espera


def buscar_indice_aeronave(codigo_buscado):
    indice_encontrado = -1
    contador_posicao = 0

    for i in range(len(codigos_estacionamento)):
        if codigos_estacionamento[i] == codigo_buscado:
            indice_encontrado = contador_posicao
        contador_posicao = contador_posicao + 1

    return indice_encontrado


def codigo_ja_esta_estacionado(codigo_buscado):
    indice = buscar_indice_aeronave(codigo_buscado)

    contador_existe = 0
    if indice != -1:
        contador_existe = 1

    return contador_existe


def solicitar_vaga(momento_atual):
    global total_estacionamentos_sucesso

    codigo_digitado = input("Digite o codigo da aeronave: ")

    duplicado = codigo_ja_esta_estacionado(codigo_digitado)
    em_espera = 0
    for i in range(len(codigo_espera)):
        if codigo_espera[i] == codigo_digitado:
            em_espera = 1

    if duplicado == 1 or em_espera == 1:
        print("Este codigo de aeronave ja esta no estacionamento ou na fila de espera.")
        return

    tem_vaga = existe_vaga_livre()

    if tem_vaga == 1:
        codigos_estacionamento.append(codigo_digitado)
        horarios_entrada.append(momento_atual)
        total_estacionamentos_sucesso = total_estacionamentos_sucesso + 1
        print(f"Aeronave {codigo_digitado} estacionada com sucesso.")
        return

    tem_espera = existe_aeronave_na_espera()

    if tem_espera == 0:
        codigo_espera.append(codigo_digitado)
        horario_espera.append(momento_atual)
        print(f"Estacionamento cheio. Aeronave {codigo_digitado} colocada na fila de espera.")
        return

    print(f"Estacionamento e fila de espera cheios. Aeronave {codigo_digitado} redirecionada para outro aeroporto.")


def calcular_valor_diaria(quantidade_dias):
    valor_calculado = 0.0

    if quantidade_dias < LIMITE_DIAS_DIARIA:
        valor_calculado = quantidade_dias * VALOR_DIARIA_CURTA
    else:
        valor_calculado = quantidade_dias * VALOR_DIARIA_LONGA

    return valor_calculado


def remover_aeronave_do_vetor(indice_remover):
    novos_codigos = []
    novos_horarios = []

    for i in range(len(codigos_estacionamento)):
        if i != indice_remover:
            novos_codigos.append(codigos_estacionamento[i])
            novos_horarios.append(horarios_entrada[i])

    codigos_estacionamento.clear()
    horarios_entrada.clear()

    for i in range(len(novos_codigos)):
        codigos_estacionamento.append(novos_codigos[i])
        horarios_entrada.append(novos_horarios[i])


def realocar_fila_de_espera():
    tem_espera = existe_aeronave_na_espera()

    if tem_espera == 1:
        codigo_promovido = codigo_espera[0]
        horario_promovido = horario_espera[0]

        codigos_estacionamento.append(codigo_promovido)
        horarios_entrada.append(horario_promovido)

        codigo_espera.clear()
        horario_espera.clear()

        print(f"Aeronave {codigo_promovido} saiu da fila de espera e foi alocada em uma vaga.")


def retirar_aeronave(momento_atual):
    global total_retiradas
    global valor_em_caixa

    codigo_digitado = input("Digite o codigo da aeronave para retirada: ")

    indice_encontrado = buscar_indice_aeronave(codigo_digitado)

    if indice_encontrado == -1:
        print(f"Aeronave {codigo_digitado} nao foi encontrada no estacionamento.")
        return

    momento_entrada = horarios_entrada[indice_encontrado]
    dias_estacionado = calcular_dias_estacionado(momento_entrada, momento_atual)
    valor_cobrado = calcular_valor_diaria(dias_estacionado)

    remover_aeronave_do_vetor(indice_encontrado)

    total_retiradas = total_retiradas + 1
    valor_em_caixa = valor_em_caixa + valor_cobrado

    print(f"Aeronave {codigo_digitado} retirada do estacionamento.")
    print(f"Data de entrada: {momento_entrada.strftime('%d/%m/%Y %H:%M')}")
    print(f"Data de retirada: {momento_atual.strftime('%d/%m/%Y %H:%M')}")
    print(f"Dias estacionado: {dias_estacionado}")
    print(f"Valor cobrado: R$ {valor_cobrado:.2f}")

    realocar_fila_de_espera()


def retirar_todas_aeronaves(momento_atual):
    global total_retiradas
    global valor_em_caixa

    quantidade_presente = contar_vagas_ocupadas()

    if quantidade_presente == 0:
        print("Nao ha aeronaves estacionadas para retirar.")
    else:
        codigos_para_retirar = []
        horarios_para_calcular = []

        for i in range(len(codigos_estacionamento)):
            codigos_para_retirar.append(codigos_estacionamento[i])
            horarios_para_calcular.append(horarios_entrada[i])

        for i in range(len(codigos_para_retirar)):
            dias_estacionado = calcular_dias_estacionado(horarios_para_calcular[i], momento_atual)
            valor_cobrado = calcular_valor_diaria(dias_estacionado)

            valor_em_caixa = valor_em_caixa + valor_cobrado
            total_retiradas = total_retiradas + 1

            print(f"Aeronave {codigos_para_retirar[i]} retirada. Dias: {dias_estacionado} | Valor: R$ {valor_cobrado:.2f}")

        codigos_estacionamento.clear()
        horarios_entrada.clear()

        print("Todas as aeronaves foram retiradas do estacionamento.")

    tem_espera = existe_aeronave_na_espera()
    if tem_espera == 1:
        codigo_espera.clear()
        horario_espera.clear()
        print("A fila de espera tambem foi esvaziada.")


def mostrar_aeronaves_estacionadas():
    quantidade_presente = contar_vagas_ocupadas()

    if quantidade_presente == 0:
        print("Nao ha aeronaves estacionadas no momento.")
    else:
        print(f"Total de aeronaves estacionadas: {quantidade_presente}")
        for i in range(len(codigos_estacionamento)):
            data_formatada = horarios_entrada[i].strftime('%d/%m/%Y %H:%M')
            print(f"Vaga {i + 1} | Codigo: {codigos_estacionamento[i]} | Entrada: {data_formatada}")

    tem_espera = existe_aeronave_na_espera()
    if tem_espera == 1:
        data_espera_formatada = horario_espera[0].strftime('%d/%m/%Y %H:%M')
        print(f"Fila de espera | Codigo: {codigo_espera[0]} | Entrada: {data_espera_formatada}")
    else:
        print("Fila de espera vazia.")


def adiantar_tempo(momento_atual):
    print("Adiantar tempo em:")
    print("1. Dias")
    print("2. Meses")
    opcao_escolhida = input("Escolha uma opcao: ")

    novo_momento = momento_atual

    if opcao_escolhida == "1":
        quantidade_dias = int(input("Quantos dias deseja adiantar? "))
        novo_momento = adiantar_tempo_em_dias(momento_atual, quantidade_dias)
        print(f"Tempo adiantado em {quantidade_dias} dia(s).")
    elif opcao_escolhida == "2":
        quantidade_meses = int(input("Quantos meses deseja adiantar? "))
        novo_momento = adiantar_tempo_em_meses(momento_atual, quantidade_meses)
        print(f"Tempo adiantado em {quantidade_meses} mes(es).")
    else:
        print("Opcao invalida. O tempo nao foi alterado.")

    return novo_momento


def mostrar_informacoes_tempo(momento_inicial, momento_atual):
    diferenca = momento_atual - momento_inicial

    print(f"Data e hora inicial do sistema: {momento_inicial.strftime('%d/%m/%Y %H:%M')}")
    print(f"Data e hora atual: {momento_atual.strftime('%d/%m/%Y %H:%M')}")
    print(f"Total de dias desde o inicio: {diferenca.days}")


def gerar_grafico():
    vagas_ocupadas = contar_vagas_ocupadas()
    vagas_livres = CAPACIDADE_MAXIMA - vagas_ocupadas
    ocupacao_espera = existe_aeronave_na_espera()

    categorias = ["Vagas ocupadas", "Vagas livres", "Fila de espera"]
    valores = [vagas_ocupadas, vagas_livres, ocupacao_espera]
    cores = ["#D85A30", "#1D9E75", "#BA7517"]

    plt.figure(figsize=(7, 5))
    plt.bar(categorias, valores, color=cores)
    plt.title("Situacao atual do estacionamento de aeronaves")
    plt.ylabel("Quantidade")
    plt.ylim(0, max(CAPACIDADE_MAXIMA, CAPACIDADE_ESPERA) + 1)

    for i in range(len(valores)):
        plt.text(i, valores[i] + 0.1, str(valores[i]), ha="center")

    nome_arquivo = "grafico_estacionamento.png"
    plt.savefig(nome_arquivo)
    plt.close()

    print(f"Grafico gerado e salvo como '{nome_arquivo}'.")


def mostrar_resumo_final():
    print("Encerrando o sistema de gerenciamento de estacionamento de aeronaves.")
    print(f"Total de estacionamentos realizados com sucesso: {total_estacionamentos_sucesso}")
    print(f"Total de retiradas de aeronaves: {total_retiradas}")
    print(f"Valor total em caixa: R$ {valor_em_caixa:.2f}")


def mostrar_menu():
    print("")
    print(" MENU - ESTACIONAMENTO PARA AERONAVES ")
    print("1. Solicitar uma vaga")
    print("2. Retirar aeronave")
    print("3. Retirar todas aeronaves")
    print("4. Mostrar todas as aeronaves")
    print("5. Adiantar o tempo")
    print("6. Mostrar informações do tempo")
    print("7. Gráfico")
    print("8. Sair")


def main():
    global tempo_atual

    momento_inicial = obter_tempo_inicial()
    tempo_atual = momento_inicial

    opcao_digitada = ""

    while opcao_digitada != "8":
        mostrar_menu()
        opcao_digitada = input("Escolha uma opcao: ")

        if opcao_digitada == "1":
            solicitar_vaga(tempo_atual)
        elif opcao_digitada == "2":
            retirar_aeronave(tempo_atual)
        elif opcao_digitada == "3":
            retirar_todas_aeronaves(tempo_atual)
        elif opcao_digitada == "4":
            mostrar_aeronaves_estacionadas()
        elif opcao_digitada == "5":
            tempo_atual = adiantar_tempo(tempo_atual)
        elif opcao_digitada == "6":
            mostrar_informacoes_tempo(momento_inicial, tempo_atual)
        elif opcao_digitada == "7":
            gerar_grafico()
        elif opcao_digitada == "8":
            mostrar_resumo_final()
        else:
            print("Opcao invalida. Tente novamente.")

main()
