# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para divisão
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."
# Função para multiplicação
def multiplicacao(x, y):
    return x * y
    # Função principal
def calculadora():
    lista_historico = []
    while True:
        print("\nDigite a operação (+, -, *, /), 'hist' para ver o histórico ou 'sair' para encerrar.")
        op = input("Operação: ")

        if op == "sair":
            print("Encerrando a calculadora.")
            break
        elif op == "hist":
            print("Histórico de resultados:", lista_historico)
            continue

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if op == '+':
            resultado = soma(num1, num2)
            print("Resultado da soma:", resultado)
            lista_historico.append(resultado)
        if op == '-':
            resultado = subtracao(num1, num2)
            print("Resultado da subtração:", resultado)
            lista_historico.append(resultado)
        if op == '/':
            resultado = divisao(num1, num2)
            print("Resultado da divisão:", resultado)
            lista_historico.append(resultado)
        if op == '*':
            resultado = multiplicacao(num1, num2)
            print("Resultado da multiplicação:", resultado)
            lista_historico.append(resultado)
        else:
            print("Operação inválida. Tente novamente.")

# Executa a calculadora
calculadora()

