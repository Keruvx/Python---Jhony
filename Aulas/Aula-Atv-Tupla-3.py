meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho"
        "junho", "agosto", "setembro", "outubro", "novembro", "dezembro")

print ("===Meses do ano===")


while True:
    numero  = int(input("Digite um numero entre 1 e 12 para saber o mês: (-1 para encerrar)"))
    if numero == -1:
        break

    if numero >= 1 and numero <= 12:

        print(f"O mês ai oh: {meses[numero - 1]}")
    else:
        print("Tem esse numero não")
