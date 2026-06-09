 
def ler_codigo_rfid(numero):
    codigo = int(input(f"Digite o código RFID {numero}: "))
 
    if codigo > 1000:
        return codigo
 
    print("Código inválido! O código deve ser maior que 1000. Tente novamente.")
    return ler_codigo_rfid(numero)
 
def ler_todos_rfid():
    codigos = []
 
    for i in range(10):
        codigo = ler_codigo_rfid(i + 1)
        codigos.append(codigo)
 
    return codigos
 
def exibir_rfid(codigos):
    print(f"\nCódigos RFID cadastrados: {codigos}")
 
def main():
    codigos = ler_todos_rfid()
    exibir_rfid(codigos)
 
main()
