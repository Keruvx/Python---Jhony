#Append-Ex:(Append(" ") - Metodo que serve para adicionar um novo elemento ao final da lista)
#Remove-Ex:(Remove(" ") - Metodo que serve para remover um nome da lista)
paises = ["Brasil","Chile"]

print (paises)
paises.append("Madagascar")
print ("Pais adicionada")
print (paises)
paises.remove("Chile")
print ("Pais apagado")
print (paises)

if "Brasil" in paises:
    paises.remove("Brasil")
    print(f"Pais removido com sucesso! {paises}")
else:
    print("Pais não existe")

#Len() - Metodo que serve para contar a quantidade de caracteres, numeros, letras, palavras...
#Sum() - Metodo que serve para somar os elementos numericos

numeros = [10,20,30]
print("Quantidade de numeros: ", len(numeros))


notas = [7.5, 8.5, 10]
print("Soma das notas é: ",sum(notas))
print(f"A media de notas é: 2:.f {sum(notas)/len(notas)}", sum(notas)/len(notas))

