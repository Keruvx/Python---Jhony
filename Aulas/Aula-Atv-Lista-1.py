alunos = []

while True:
          print("\nMenu de opções")
          print("1 - Para adicionar nome de alunos: ")
          print("2 - Para exibir quantos alunos estão listados: ")
          print("3 - Para ver a lista completa de alunos")
          print("4 - Para sair do programa")

          opcao = int(input("Escolha uma opção: "))
          if opcao == 1:
               while True:
                    aluno = (input("Digite um nome (Sair voltar ao menu): "))
                    if aluno.lower() == "sair":
                         break
                    alunos.append(aluno)

          elif opcao == 2:
               print(f"A quantidade de alunos é:", len(alunos))

          elif opcao == 3:
               print(f"Lista completa de alinos: {alunos}")

          elif opcao == 4:
               print("Programa encerrado")
               break
          else:
               print("Tem essa opção não.")