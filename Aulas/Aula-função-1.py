# -----------------------------------------------
# --- Funções  ---
# -----------------------------------------------


def pegar_notas():
        n1 = float(input("Digite sua nota 1: "))
        n2 = float(input("Digite sua nota 2: "))
        n3 = float(input("Digite sua nota 3: "))
        return n1, n2, n3

def calcular_media(n1 ,n2,n3 ):
        return (n1 ,n2,n3 )/3

def verficar_situacao(media):
        if media >= 7:
                return "Aprovado"
        elif media >= 5 and media <= 7:
                return "Recuperação"
        else:
                return "Reprovado"
        

nome = input("Nome do aluno: ")
notas = pegar_notas ()
media = calcular_media(*notas)
situacao = verficar_situacao(media)

print(f"\nAluno: {nome}")
print(f"Media: {media:.2f} - Situação {situacao}")

