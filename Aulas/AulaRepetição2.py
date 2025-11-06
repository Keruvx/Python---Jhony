#05/11/25
#Inicia o loop que vai se repetir enquanto a condição for verdadeira
while True: #True é uma condição booleana que sempre é verdadeiro, logo esse loop será infinito
    nome = input("Usuário: ")
    senha = input("Senha: ")
    #Condição que faz a comparação para verificar se as condições são verdadeiras
    if nome == "admin" and senha == "1234":
       print("Login Realizado Com Sucesso!")
       break #Comando que interrompe imediatamente o loop
    else:
        print("Usuário ou senha incorretas! Tente novamente...")
