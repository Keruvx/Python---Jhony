nomes = []
salarios = []

print("\nPrograma\n\n")
print("Digite 'Sair' para encerrar a adição de nomes.")

while True:
     nome = input("Informe seu nome: ")
     if nome.lower() == "sair":
          break
     salario = int(input("Informe o salario: "))
     nomes.append(nome)
     salarios.append(salario)

print(f"Quantidade de funcionarios: ", len(nomes))
print(f"Media salarial: {sum(salarios)/len(nomes):.2f}")
print(f"Maior salario {max(salarios)}")
print(f"Menor salario {min(salarios)}")
