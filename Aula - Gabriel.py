import random

secreto = random.randint(1, 100)
tentativas = 3

print(" === Desafio do número secreto === ")
print(" === Desafio do número secreto === ")

while tentativas > 0:
    chute = int(input("Seu chute:"))

    if chute == secreto:
        print("Você acertou")
        break 
    elif chute < secreto:
            print("chute muito baixo")
    else:
            print("chuto muito alto")

    tentativas -= 1
    print(f"tentativas restante: {tentativas}\n")

if tentativas == 0:
    print(f"Acabaram as tentativas, o numero era: {secreto}")