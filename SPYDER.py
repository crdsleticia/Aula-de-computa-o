# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:13:39 2024

@author: 202102322286
"""

# Variáveis para armazenar quatro números
numero1 = 20
numero2 = 40
numero3 = 50
numero4 = 60

# Variável para armazenar uma frase
frase = "Aula de computação maravilhosa."

# Variável para armazenar uma palavra
palavra = "exemplo"

# Calcula a média aritmética entre os quatro números
media = (numero1 + numero2 + numero3 + numero4) / 4

# Calcula o quadrado de um dos números (escolhendo o primeiro número como exemplo)
quadrado = numero1 ** 2

# Calcula o dobro de um dos números (escolhendo o segundo número como exemplo)
dobro = numero2 * 2

# Conta a quantidade de letras da palavra
quantidade_letras = len(palavra)

# Conta a quantidade de espaços em branco da frase
quantidade_espacos = frase.count(' ')

# Verifica se o primeiro número é maior que o segundo
primeiro_maior_que_segundo = numero1 > numero2

# Encontra o maior número
maior_numero = max(numero1, numero2, numero3, numero4)

# Imprime os resultados
print(f"Média aritmética: {media}")
print(f"Quadrado do primeiro número: {quadrado}")
print(f"Dobro do segundo número: {dobro}")
print(f"Quantidade de letras da palavra: {quantidade_letras}")
print(f"Quantidade de espaços em branco da frase: {quantidade_espacos}")
print(f"O primeiro número é maior que o segundo? {'Sim' if primeiro_maior_que_segundo else 'Não'}")
print(f"O maior número é: {maior_numero}")
