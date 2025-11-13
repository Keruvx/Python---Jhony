ns = ()

while True:
    n = int(input("Digite um numero: "))
    ns += (n, )
    if (len(ns) == 5):
        break

print("Numeros digitados: ", ns)
print("Maior numero: ", max(ns))
print("Menor numero: ", min(ns))
#print("Numeros com 5", ns)
for i, valor in enumerate(ns):
    if valor == 5:
        print(f"O número 5 está no índice {i}")