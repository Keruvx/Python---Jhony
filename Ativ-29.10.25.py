##Simulador de emprestimo Bancario
print("===Posso comprar?===")


##Primeiro vem o nome da variavel (Nome) depois (Input) para perguntar ao usuario
nome = input("Informe seu nome: ")
##float foi usado pq ser um numero Real
renda = float(input("Informe sua renda: R$"))
valorSolicitado = float(input("Informe valor de emprestimo que deseja: R$"))
parcela = int(input("Informe o número de parcelas: "))
historico = input("Possui nome sujo? (sim/não): ")

#Calculo do valor da parcela
valorParcela = (valorSolicitado/parcela)


print(f"\nCliente: {nome}")
print(f"Valor do empréstimo: R$ {valorSolicitado:.2f}")
print(f"Quantidade de parcelas {parcela}x de R$ {valorParcela:.2f}")

if historico == "sim":
    print("Emprestimo NEGADO!!")
else:
    #Verifica se a parcela não ultrapassa 30% da renda
    if valorSolicitado > renda*0.3:
        print("Emprestimo NEGADO!! (Valor da renda e menor que o valor da parcela)")
    else:
        #Verificar o valor do emprestimo em relação a renda
        if valorSolicitado > renda*20:
            print("Emprestimo NEGADO!! Valor solicitado muito alto para a renda informada.")
        elif renda >= 5000 and valorSolicitado <= 10000:
            print("Emprestimo APROVADO!")
        elif renda >= 3000 and renda < 5000:
            print("Empretimo APROVADO! - Com taxa padrão.")
        else:
            print("Emprestimo APROVADO! - Com taxa elevada")

print("\n=== Processo de emprestimo encerrado ===\n")


