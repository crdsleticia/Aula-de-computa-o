def salvar_nome_arquivo():
    # Solicita ao usuário que insira seu nome
    nome = input("Por favor, digite seu nome: ")
    
    # Abre um arquivo no modo de escrita. Se o arquivo não existir, ele será criado.
    # Se já existir, o conteúdo anterior será substituído.
    with open("nome_usuario.txt", "w") as arquivo:
        # Escreve o nome no arquivo
        arquivo.write(nome)
    
    print("Seu nome foi salvo com sucesso no arquivo nome_usuario.txt.")

# Chama a função para executar
salvar_nome_arquivo()

