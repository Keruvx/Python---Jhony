'  ####                      #     #                 ## '
'  #                         #                      #  # '
'  ###    ###  #  #   ###   ###   ##    ###    ##   #      ###  ###'
'  #     #  #  #  #  ##      #     #    #  #  #  #  #     #  #  #  #'
'  #     # ##  #  #    ##    #     #    #  #  #  #  #  #  # ##  #'
'  #      # #   ###  ###      ##  ###   #  #   ##    ##    # #  #'



loginAdmin = [
    ("admin", )

]
senhaAdlmin = [
    ("1234", )

]
loginUsuario = [
    ("aaa", )
]
senhaUsuario = [
    ("aaa", )
]

def menu():
    print("Bem-Vindo a FaustinoCar\n")
    print("1 - Entrar")
    print("2 - Cadastrar")

def menuLogin():
        entraL = input("Login: ")
        entraS = input("Senha: ")
        if entraL == loginUsuario[0] and entraS == senhaUsuario[0]:
            print("Teste")
        elif entraL != loginUsuario[0] and entraS != senhaUsuario[0]:
            print("pretinho")
        else:
            print (" fuck") 
    

def menuCadastro():
    ll = input("Informe Login: ")
    ss = input("Informe Senha: ")
    loginUsuario.append(ll)
    senhaUsuario.append(ss)


while True:
    menu()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            menuLogin()
        case "2":
            menuCadastro()


