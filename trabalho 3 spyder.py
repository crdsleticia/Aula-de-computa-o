def lista_de_compras():
    # Solicita ao usuário que digite os itens da lista de compras, separados por vírgula
    itens = input("Digite os itens da lista de compras, separados por vírgula: ")
    
    # Divide a string de entrada em uma lista, usando vírgula como delimitador
    lista_itens = itens.split(',')
    
    # Remove espaços extras nos itens da lista
    lista_itens = [item.strip() for item in lista_itens]
    
    # Imprime cada item da lista em uma nova linha
    for index, item in enumerate(lista_itens):
        print(f"Item {index + 1}: {item}")

# Chamar a função para testar
lista_de_compras()
