def imprimir_conteudo_arquivo():
    # Solicita ao usuário que digite o nome do arquivo de texto
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    
    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r') as arquivo:
            # Lê todo o conteúdo do arquivo
            conteudo = arquivo.read()
        
        # Imprime o conteúdo do arquivo
        print("Conteúdo do arquivo:")
        print(conteudo)
    except FileNotFoundError:
        # Caso o arquivo não seja encontrado, imprime uma mensagem de erro
        print("Arquivo não encontrado.")
    except Exception as e:
        # Captura outras exceções que possam ocorrer e imprime a mensagem de erro
        print("Ocorreu um erro:", e)

# Chama a função para testar
imprimir_conteudo_arquivo()


