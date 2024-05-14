def bombom(dinheiro, preco):
    numero_bombons = dinheiro // preco  # Calcula o número de bombons que podem ser comprados
    troco = dinheiro % preco  # Calcula o troco
    return numero_bombons, troco  # Retorna uma tupla com o número de bombons e o troco

# Exemplo de uso da função
dinheiro_de_joaozinho = 2540
preco_do_bombom = 25

numero_bombons, troco = bombom(dinheiro_de_joaozinho, preco_do_bombom)
print(f"Joãozinho pode comprar {numero_bombons} bombons e sobrarão R${troco} de troco.")
