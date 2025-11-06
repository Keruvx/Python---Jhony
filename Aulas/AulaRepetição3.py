#05/11/25
print("\nCADASTRO DE USUÁRIO\n")
UserName = input("Login: ").strip().lower() #Strip = Ele tira o espaço / Lower = Arruma as letras maiusculas e minusculas


while True:
    UserSenha = input("Senha: (Máx 8 Caracteres)").strip()
    
    if len(UserSenha) <= 8:
        print("\nUsuário cadastrado com sucesso!\n")
        break
    else:
        print("Senha muito longa!")
#Inicia o loop que vai se repetir enquanto a condição for verdadeira
while True: #True é uma condição booleana que sempre é verdadeiro, logo esse loop será infinito
    print("Entrar")
    nome = input("Login: ").strip().lower()
    senha = input("Senha: ").strip()
    
    #Condição que faz a comparação para verificar se as condições são verdadeiras
    if nome == UserName and senha == UserSenha:
       print(f"\n\nLogin Realizado Com Sucesso!\n\nBem-Vindo {UserName}")
       break #Comando que interrompe imediatamente o loop
    else:
        print("Usuário ou senha incorretas! Tente novamente...")
