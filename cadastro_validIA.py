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
    oiii
    