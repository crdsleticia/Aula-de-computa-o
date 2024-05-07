def converter_celsius_para_fahrenheit():
    # Solicita ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    
    # Converte a temperatura para Fahrenheit usando a fórmula
    fahrenheit = (celsius * 9/5) + 32
    
    # Imprime o resultado da conversão
    print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.")

# Chamar a função para testar
converter_celsius_para_fahrenheit()

