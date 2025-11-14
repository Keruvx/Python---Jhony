nomes = ()

while True:
    nome = input("Digite um nome: ")
    nomes += (nome, )
    if (len(nomes) == 5):
        #print("passei aqui desgraça")comando de texte do grabriel kk
        break

print("Primeiro aluno",  nomes[0])
print("Ultimo aluno", nomes[4])
print("E um total de ", len(nomes))