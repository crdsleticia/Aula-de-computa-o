def coletar_nomes():
    nomes = []  # Lista para armazenar os nomes
    while True:  # Loop infinito para coletar nomes
        nome = input("Digite um nome ou 'sair' para terminar: ")
        if nome == "sair":  # Verifica se o usuário deseja sair
            break
        nomes.append(nome)  # Adiciona o nome à lista

    print("\nLista de Nomes:")
    for nome in nomes:
        print(nome)  # Imprime cada nome individualmente

# Chama a função para testar
coletar_nomes()

