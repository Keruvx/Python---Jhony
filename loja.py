print("\n --- Lojinha do japa ---")
valor = float(input("Digite o valor total da compra (R$): "))
formaPagamento = input("Forma de pagamento (dinheiro/debito/credito/pix): ")

if formaPagamento == "dinheiro":
    total = valor*0.90
    print(f"Pagamento à vista em dinheiro. Desconto de 10% - Total {total:.2f}")
elif formaPagamento == "pix":
    if valor >= 1000:
        total = valor*0.85
        print(f"Pagamento via pix: Desconto de 15% - Total R${total:.2f}")
    elif valor >= 500 and valor < 1000:
        total = valor*0.90
        print(f"Pagamento via pix: Desconto de 10% - Total R${total:.2f}")
    else:
        total = valor*0.95
        print(f"Pagamento via pix: Desconto de 5% - Total R${total:.2f}")
elif formaPagamento == "debito":
    total = valor 
    print(f"Pagamento a vista no cartão de debito - Total R${total:.2f}")
elif formaPagamento == "credito":
    parcelas = int(input("Quantas parcelas: "))
    if parcelas <= 3:
        total =  valor
        print(f"Pagamento no cartão de credito em {parcelas}X - Valor Total R${total:.2f} - Valor da parcela R${total/parcelas}")
    elif 4 <= parcelas <=6:
        total = valor*1.10
        print(f"Pagamento no cartão de credito em {parcelas}X - Valor Total R${total:.2f} - Valor da parcela R${total/parcelas}")
    else:
        total = valor*1.20
        print(f"Pagamento no cartão de credito em {parcelas}X - Valor Total R${total:.2f} - Valor da parcela R${total/parcelas}")
 










