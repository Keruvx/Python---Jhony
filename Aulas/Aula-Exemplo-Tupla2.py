#Criação de programa que permita que o usuario consulte o preço de um produto digitando o nome

#Duas tuplas paralelas: uma com nomes dos produtos e outroa com o valor
produto = ("arroz","feijão","macarrão","leite","pão","ovo")
preco = (5.50, 7.90, 4.20, 6.30, 3.00, 19.96)

#Exibe a lista completa de produtos com seus preços
print("\n==== LISTA DE PRODUTOS ====")

for i in range(len(produto)):
    #Percorre as posições (0 até 5) exibe o produto e o preço corresponde

    print(f"{produto[i]} - R$ {preco[i]:.2f}")

#Inicial um loop para permitir varias consultas do usuario
while True:
    nome = input("\\nDigite o nome produto para ver o preço (ou 'sair')")
    #Metodo .lower() transforma o texto em minusculos para evitar erro de comparação

    #Se o usuario digitar 'sair', o programa termina
    if nome == "sair":
        print(f"Programa encerrado.")
        break
    
    if nome in produto:
        indice = produto.index(nome) 

        print(f"O preço de {nome} é R$ {preco[indice]:.2f}.")
    else:
        print("Produto não encontrado.")




