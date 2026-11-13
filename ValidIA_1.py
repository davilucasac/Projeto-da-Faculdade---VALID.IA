# TUPLA: Categorias fixas e imutáveis para organizar os temas
TEMAS_DISPONIVEIS = ("Programação", "Ciências", "História", "Idiomas", "Outros")

# LISTA: Nosso "banco de dados" em memória que guardará vários dicionários
historico_perguntas = []

# VARIÁVEL GLOBAL: Controle de ID único para cada pergunta
proximo_id = 1


def exibir_menu():
    """Exibe as opções do sistema utilizando uma tupla."""
    opcoes = (
        "1 - Criar nova pergunta (Create)",
        "2 - Listar histórico de perguntas (Read)",
        "3 - Atualizar pergunta/tema (Update)",
        "4 - Deletar pergunta (Delete)",
        "5 - Sair do sistema"
    )
    print("\n" + "=" * 40)
    print("   HISTÓRICO DE PERGUNTAS PARA IA")
    print("=" * 40)
    for opcao in opcoes:
        print(opcao)
    print("=" * 40)


def escolher_tema():
    """Função auxiliar que usa 'while' e 'try/except' para validar a escolha da tupla."""
    while True:
        print("\nTemas disponíveis:")
        # Loop 'for' com enumerate para mostrar índice e valor da tupla
        for indice, tema in enumerate(TEMAS_DISPONIVEIS, start=1):
            print(f"  {indice}. {tema}")
        
        try:
            escolha = int(input("Escolha o número do tema: "))
            if 1 <= escolha <= len(TEMAS_DISPONIVEIS):
                return TEMAS_DISPONIVEIS[escolha - 1]
            else:
                print(f"[Aviso] Escolha um número entre 1 e {len(TEMAS_DISPONIVEIS)}.")
        except ValueError:
            print("[Erro] Entrada inválida! Por favor, digite apenas números.")


# ---------------------------------------------------------
# 1. CREATE (Criar e armazenar)
# ---------------------------------------------------------
def criar_pergunta(lista_dados, id_atual):
    """Recebe a lista e o ID por parâmetro, cria um dicionário e o adiciona à lista."""
    print("\n--- NOVA PERGUNTA ---")
    tema = escolher_tema()
    
    pergunta = input("Digite a pergunta feita à IA: ").strip()
    while not pergunta:  # Garante que o usuário não salve um texto vazio
        print("[Aviso] A pergunta não pode ficar em branco.")
        pergunta = input("Digite a pergunta feita à IA: ").strip()

    # DICIONÁRIO: Estrutura que representa um registro completo
    novo_registro = {
        "id": id_atual,
        "tema": tema,
        "pergunta": pergunta
    }
    
    lista_dados.append(novo_registro)
    print(f"\n[Sucesso] Pergunta registrada com o ID #{id_atual}!")
    return id_atual + 1  # Retorna o próximo ID incrementado


# ---------------------------------------------------------
# 2. READ (Ler o que foi salvo)
# ---------------------------------------------------------
def ler_historico(lista_dados):
    """Percorre a lista de dicionários e exibe os dados formatados."""
    print("\n--- HISTÓRICO SALVO ---")
    if not lista_dados:
        print("Nenhuma pergunta cadastrada no momento.")
        return False  # Retorna False indicando que a lista está vazia
    
    for item in lista_dados:
        print(f"ID: #{item['id']} | Tema: [{item['tema']}]")
        print(f"Pergunta: {item['pergunta']}")
        print("-" * 40)
    return True


# ---------------------------------------------------------
# 3. UPDATE (Atualizar pergunta ou tema)
# ---------------------------------------------------------
def atualizar_pergunta(lista_dados):
    """Busca um registro pelo ID e permite corrigir o texto ou o tema."""
    print("\n--- ATUALIZAR PERGUNTA ---")
    # Reutiliza a função de leitura; se estiver vazia, encerra a função
    if not ler_historico(lista_dados):
        return

    try:
        id_busca = int(input("Digite o ID da pergunta que deseja corrigir: "))
        
        for item in lista_dados:
            if item["id"] == id_busca:
                print(f"\nEditando ID #{id_busca}: '{item['pergunta']}'")
                
                # Atualiza a pergunta
                nova_pergunta = input("Digite a pergunta corrigida (ou Enter para manter a atual): ").strip()
                if nova_pergunta:
                    item["pergunta"] = nova_pergunta
                
                # Pergunta se deseja alterar o tema também
                alterar_tema = input("Deseja alterar o tema? (s/n): ").strip().lower()
                if alterar_tema == 's':
                    item["tema"] = escolher_tema()
                
                print("\n[Sucesso] Registro atualizado com sucesso!")
                return
        
        print(f"[Aviso] Nenhum registro encontrado com o ID #{id_busca}.")
        
    except ValueError:
        print("[Erro] O ID deve ser um número inteiro.")


# ---------------------------------------------------------
# 4. DELETE (Deletar informação)
# ---------------------------------------------------------
def deletar_pergunta(lista_dados):
    """Remove um dicionário da lista com base no ID informado."""
    print("\n--- DELETAR PERGUNTA ---")
    if not ler_historico(lista_dados):
        return

    try:
        id_busca = int(input("Digite o ID da pergunta que deseja excluir: "))
        
        for i, item in enumerate(lista_dados):
            if item["id"] == id_busca:
                confirmacao = input(f"Tem certeza que deseja excluir '{item['pergunta']}'? (s/n): ").strip().lower()
                if confirmacao == 's':
                    lista_dados.pop(i)
                    print(f"\n[Sucesso] Pergunta #{id_busca} removida do histórico.")
                else:
                    print("\nOperação cancelada.")
                return
                
        print(f"[Aviso] Nenhum registro encontrado com o ID #{id_busca}.")
        
    except ValueError:
        print("[Erro] O ID deve ser um número inteiro.")


# ---------------------------------------------------------
# FLUXO PRINCIPAL DO PROGRAMA
# ---------------------------------------------------------
def iniciar_sistema():
    global proximo_id
    
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                proximo_id = criar_pergunta(historico_perguntas, proximo_id)
            elif opcao == 2:
                ler_historico(historico_perguntas)
            elif opcao == 3:
                atualizar_pergunta(historico_perguntas)
            elif opcao == 4:
                deletar_pergunta(historico_perguntas)
            elif opcao == 5:
                print("\nEncerrando o sistema. Até mais!")
                break
            else:
                print("[Aviso] Opção inválida! Digite um número de 1 a 5.")
                
        except ValueError:
            print("[Erro] Entrada inválida! Digite apenas o número da opção.")
        except KeyboardInterrupt:
            # Trata caso o usuário aperte Ctrl+C no terminal para fechar o programa
            print("\n\nPrograma interrompido pelo usuário. Saindo...")
            break


# Ponto de entrada do script
if __name__ == "__main__":
    iniciar_sistema()
    gabi