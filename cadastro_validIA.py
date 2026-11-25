def criar_cadastro(cadastros):
    """Função para criar um novo cadastro (CREATE)"""
    print("\n--- NOVO CADASTRO ---")
    nome = input("Digite o NOME: ").strip()
    email = input("Digite o E-MAIL: ").strip()
    usuario = input("Digite o NOME DE USUÁRIO: ").strip()
    cpf = input("Digite o CPF (apenas números): ").strip()
    
    
    for item in cadastros:
        if item['cpf'] == cpf:
            print("\n[ERRO] Já existe um cadastro com este CPF!")
            return
            
    
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
    
    
def atualizar_cadastro(cadastros):
    """Função para atualizar um cadastro existente (UPDATE)"""
    print("\n--- ATUALIZAR CADASTRO ---")
    if not cadastros:
        print("Nenhum cadastro disponível para atualizar.")
        return
        
    cpf_busca = input("Digite o CPF do usuário que deseja atualizar: ").strip()
    encontrado = False
    
    for user in cadastros:
        if user['cpf'] == cpf_busca:
            encontrado = True
            print(f"\nUsuário encontrado: {user['nome']}")
            print("Deixe o campo em branco se não quiser alterar a informação.")
            
            novo_nome = input(f"Novo Nome [{user['nome']}]: ").strip()
            novo_email = input(f"Novo E-mail [{user['email']}]: ").strip()
            novo_usuario = input(f"Novo Usuário [{user['usuario']}]: ").strip()
            
            if novo_nome:
                user['nome'] = novo_nome
            if novo_email:
                user['email'] = novo_email
            if novo_usuario:
                user['usuario'] = novo_usuario
                
            print("\n[SUCESSO] Cadastro atualizado com sucesso!")
            break
    
    if not encontrado:
        print("\n[ERRO] Nenhum cadastro encontrado com este CPF.")

def deletar_cadastro(cadastros):
    """Função para remover um cadastro (DELETE)"""
    print("\n--- DELETAR CADASTRO ---")
    if not cadastros:
        print("Nenhum cadastro disponível para deletar.")
        return
        
    cpf_busca = input("Digite o CPF do usuário que deseja deletar: ").strip()
    removido = False
    
    for i, user in enumerate(cadastros):
        if user['cpf'] == cpf_busca:
            # Tupla contendo opções válidas de confirmação
            opcoes_confirmacao = ('s', 'sim', 'y')
            
            confirmacao = input(f"Tem certeza que deseja excluir '{user['nome']}'? (s/n): ").lower().strip()
            
            if confirmacao in opcoes_confirmacao:
                cadastros.pop(i)
                print("\n[SUCESSO] Cadastro removido com sucesso!")
            else:
                print("\n[CANCELADO] A operação de exclusão foi cancelada.")
                
            removido = True
            break
    
    if not removido:
        print("\n[ERRO] Nenhum cadastro encontrado com este CPF.")

def main():
    """Função principal que gerencia o menu e o loop do sistema"""
    cadastros = []
    
    while True:
        print("\n" + "=" * 40)
        print("        SISTEMA DE CADASTRO - CRUD")
        print("=" * 40)
        print("[1] Criar novo cadastro")
        print("[2] Listar cadastros (Read)")
        print("[3] Atualizar cadastro")
        print("[4] Deletar cadastro")
        print("[5] Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            criar_cadastro(cadastros)
        elif opcao == '2':
            listar_cadastros(cadastros)
        elif opcao == '3':
            atualizar_cadastro(cadastros)
        elif opcao == '4':
            deletar_cadastro(cadastros)
        elif opcao == '5':
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida! Escolha um número entre 1 e 5.")

if __name__ == "__main__":
    main()
