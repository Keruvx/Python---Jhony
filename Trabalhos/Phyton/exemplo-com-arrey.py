usuarios = [
    {"login": "admin", "senha": "1234"},
    {"login": "aaa", "senha": "aaa"}
]

def menu():
    print("\n=== FaustinoCar ===")
    print("1 - Entrar")
    print("2 - Cadastrar")
    print("3 - Sair")

def menuLogin():
    entraL = input("Login: ")
    entraS = input("Senha: ")

    # Percorre cada objeto dentro da lista
    for user in usuarios:
        if user["login"] == entraL and user["senha"] == entraS:
            print("\n✔ Login realizado com sucesso!")
            print(f"Bem-vindo, {entraL}!\n")
            return

    print("\n❌ Login ou senha incorretos!\n")

def menuCadastro():
    novoLogin = input("Escolha um login: ")
    novaSenha = input("Escolha uma senha: ")

    # Verifica se já existe
    for user in usuarios:
        if user["login"] == novoLogin:
            print("\n❌ Esse login já existe. Tente outro.\n")
            return

    # Adiciona dinamicamente sem índice
    usuarios.append({"login": novoLogin, "senha": novaSenha})
    print("\n✔ Usuário cadastrado com sucesso!\n")

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            menuLogin()
        case "2":
            menuCadastro()
        case "3":
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")
