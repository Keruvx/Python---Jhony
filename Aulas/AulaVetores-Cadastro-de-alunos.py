#Objetivo criar um programa de gerenciador de notas e mostrar o uso de len(),append(), sum(), remove()

#lista vazia guardar as notas

notas = []

print("==== Gerenciador de notas ====")

while True:
    print("\n Menu de Opções:")
    print("1 - Adicionar nota")
    print("2 - Remover nota")
    print("3 - Mostrar todas as notas")
    print("4 - Mostrar a quantidade e media das notas")
    print("5 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print("Nota adicionada")
    
    elif opcao == 2:
        if len(notas) == 0:
            print("Não a notas")
        else:
            print("Notas atuais: ",notas)
            remove = float(print("Informe a nota que deseja remover: "))
            if remove in notas:
                notas.remove(remove)
                print(f"Nota {remove} removida com sucesso!")
            else:
                print("Essa nota não está na lista.")

    elif opcao == 3:
        if len(notas) == 0:
            print("Não tem notas aqui")
        else:
            print("As notas que você tem são: ",notas)
    
    elif opcao == 4:
        if len(notas) == 0:
            print("Não tem notas aqui")
        else:
            quantidade = len(notas)
            soma = sum(notas)
            media = soma/quantidade
            print(f"Quantidade de notas: ",{quantidade})
            print(f"Soma das notas: ,{soma:.2f}")
            print(f"Media da turma: ,{media:.2f}")

            if media >= 7:
                print("A turma está com bom desempenho!")
            else:
                print("A turma precisa melhorar.")
                
    elif opcao == 5:
        print("Encerrando o programa. Tchau")
        break

    else:
        print("Tem essa opção não.")

