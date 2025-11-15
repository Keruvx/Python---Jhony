# -----------------------------------------------
# --- Funções  ---
# -----------------------------------------------


def casdastra_produto(estoque):
    nome = input("Nome de produto: ")
    qtd = int(input("Quantidade: "))
    estoque[nome] =  qtd
    print("Produto cadastrado")

def vender(estoque):
    nome = input("Produto para vender: ")
    if nome in estoque and estoque[nome] > 0:
        estoque[nome] -= 1
        print("Venda realizada")
    else:
        print("Produto indisponivel")

def mostrar(estoque):
    print("\n---ESTOQUE----")
    for p, q in estoque.items():
        print(f"{p}:{q}")

def menu():
    estoque = ()

    while True:
        print("\n1 - Cadastrar \n2 - Vender \n3 - Mostrar \n - Sair")

        op = int(input("Escolha:"))

        match op:
            case 1 :
                casdastra_produto(estoque)
            case 2 :
                vender(estoque)
            case 3:
                mostrar(estoque)
            case 4:
                print("Encerrando")