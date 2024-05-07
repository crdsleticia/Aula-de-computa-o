def calcular():
    # Solicita ao usuário os dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Solicita ao usuário a operação desejada
    operacao = input("Escolha a operação (+, -, * ou /): ")
    
    # Calcula o resultado com base na operação escolhida
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Adiciona uma verificação para evitar divisão por zero
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida. Escolha +, -, * ou /.")
        return
    
    # Imprime o resultado
    print("O resultado é:", resultado)

# Chama a função para execução
calcular()
