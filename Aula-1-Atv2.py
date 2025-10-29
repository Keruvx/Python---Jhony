#Atividade - 2
#Solicita ao usuário que informe a hora
hora = int(input("Digite a hora atual (0 a 23): "))

if hora <= 12:
    print("Bom dia!")
elif hora > 12 and hora < 18:
    print("Boa tarde")
else:
    print("Boa noite")