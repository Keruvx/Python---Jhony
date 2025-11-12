numeros = () #Criação de tupla com nome numeros que ira guardar numero fornecidos pelo usuario 

while True:
    n = int(input("Digite um numero (ou -1 para sair): "))
    if n == -1:
        break
    numeros += (n,)
if len(numeros) > 0:
    print("\n=== RESULTADOS ====\n")
    print(f"Numeros digitados: {numeros}")
    print(f"Quantidade: {len(numeros)}")
    print(f"Soma: {sum(numeros)}")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor numero: {min(numeros)}")

    media = sum(numeros)/len(numeros)

    if media >= 50:
        print(f"Media: {media:.2f} ->Alta!")
    else:
        print(f"Media: {media:.2f} -> Baixa!")

else:
    print("Nenhum numero foi adicionado!")

