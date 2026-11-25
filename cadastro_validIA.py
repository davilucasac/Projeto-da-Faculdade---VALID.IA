def criar_cadastro(cadastros):
    """Função para criar um novo cadastro (CREATE)"""
    print("\n--- NOVO CADASTRO ---")
    nome = input("Digite o NOME: ").strip()
    email = input("Digite o E-MAIL: ").strip()
    usuario = input("Digite o NOME DE USUÁRIO: ").strip()
    cpf = input("Digite o CPF (apenas números): ").strip()
    
    # Validação utilizando 'for' para verificar se o CPF já existe
    for item in cadastros:
        if item['cpf'] == cpf:
            print("\n[ERRO] Já existe um cadastro com este CPF!")
            return
            
    # Dicionário com as informações do usuário
    novo_usuario = {
        'cpf': cpf,
        'nome': nome,
        'email': email,
        'usuario': usuario
    }
    cadastros.append(novo_usuario)
    print(f"\n[SUCESSO] Usuário '{usuario}' cadastrado com sucesso!")

def listar_cadastros(cadastros):
    """Função para listar todos os cadastros (READ)"""
    print("\n--- LISTA DE CADASTROS ---")
    if not cadastros:
        print("Nenhum cadastro encontrado.")
    else:
        for indice, user in enumerate(cadastros):
            print("-" * 30)
            print(f"ID / Posição: {indice}")
            print(f"Nome    : {user['nome']}")
            print(f"E-mail  : {user['email']}")
            print(f"Usuário : {user['usuario']}")
            print(f"CPF     : {user['cpf']}")
        print("-" * 30)
    
    
