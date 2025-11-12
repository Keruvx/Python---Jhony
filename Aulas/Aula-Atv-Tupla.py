alunos = []

while True:
    print("\nMenu de opções")
    print("1 - Para adicionar nome de alunos: ")
    print("2 - Para exibir quantos alunos estão listados: ")
    print("3 - Para ver a lista completa de alunos")
    print("4 - Para sair do programa")

    opcao = int(input("Escolha uma opção: "))
    while True:
            if opcao == 1:
                aluno = (input("Digite um nome (Sair voltar ao menu): "))
                alunos.append(aluno)
                if aluno == "sair".lower():
                    break
            elif opcao == 2:
                 print(f"A quantidade de alunos é:", len(alunos))
                 break

            elif opcao == 3:
                 print(f"Lista completa de alinos: {alunos}")
                 break
            
            elif opcao == 4:
                 print("Encerrando o programa.")
                 break
            
            else:
                print("Tem essa opção não.")
