# --------------------------------------------------------------------------
# Parceiro de Programacao: Sistema de Gestão de Estoque v3
# - Catálogo de Armazéns (Cód + Nome)
# --------------------------------------------------------------------------

# --- Nossas Estruturas de Dados ---

# 1. Catálogo de Produtos { "cod_produto": "nome_do_produto" }
produtos = {}

# 2. (NOVO) Catálogo de Armazéns { "cod_armazem": "nome_do_armazem" }
armazens = {}

# 3. O Estoque { "cod_armazem": { "cod_produto": quantidade } }
#    Agora usa os códigos do catálogo acima como chave.
estoque = {}

# -----------------------------------------------
# --- Funções de Gestão de Catálogos ---
# -----------------------------------------------

def criar_produto(cod, nome):
    """
    Regista um novo produto no catálogo 'produtos'.
    """
    if cod in produtos:
        print(f"Erro: O produto com código '{cod}' já existe no catálogo.")
    else:
        produtos[cod] = nome
        print(f"Sucesso: Produto '{nome}' (Cód: {cod}) criado no catálogo.")

def criar_armazem(cod_armazem, nome_armazem):
    """
    (ALTERADO) Regista um novo armazém nos catálogos 'armazens' e 'estoque'.
    """
    if cod_armazem in armazens:
        print(f"Erro: O armazém com código '{cod_armazem}' já existe.")
    else:
        # Adiciona a definição (Cód -> Nome)
        armazens[cod_armazem] = nome_armazem
        # Cria o espaço de estoque (vazio) para este código
        estoque[cod_armazem] = {}
        print(f"Sucesso: Armazém '{nome_armazem}' (Cód: {cod_armazem}) criado.")

# -----------------------------------------
# --- Funções de Movimentação de Estoque ---
# (Estas funções não precisam de alteração lógica)
# -----------------------------------------

def adicionar_estoque(cod_produto, cod_armazem, quantidade):
    """
    Adiciona (dá entrada) de uma quantidade de produto em um armazém específico.
    """
    print(f"--- Tentando adicionar {quantidade} un. de '{cod_produto}' no Cód. Armazém '{cod_armazem}' ---")
    
    # Verificações
    if cod_produto not in produtos:
        print(f"Erro: Produto '{cod_produto}' não existe no catálogo. Crie o produto primeiro.")
        return
    if cod_armazem not in estoque: # Verifica se o CÓDIGO do armazém existe no 'estoque'
        print(f"Erro: Armazém '{cod_armazem}' não existe. Crie o armazém primeiro.")
        return
    if quantidade <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
        return

    # Lógica de Adição
    armazem = estoque[cod_armazem]
    quantidade_atual = armazem.get(cod_produto, 0)
    armazem[cod_produto] = quantidade_atual + quantidade
    
    nome_produto = produtos.get(cod_produto, "Desconhecido")
    nome_armazem = armazens.get(cod_armazem, "Desconhecido")
    print(f"Sucesso: Estoque de '{nome_produto}' atualizado para {armazem[cod_produto]} no armazém '{nome_armazem}'.")

def remover_estoque(cod_produto, cod_armazem, quantidade):
    """
    Remove (dá saída) de uma quantidade de produto de um armazém específico.
    """
    print(f"--- Tentando remover {quantidade} un. de '{cod_produto}' do Cód. Armazém '{cod_armazem}' ---")

    # Verificações
    if cod_produto not in produtos:
        print(f"Erro: Produto '{cod_produto}' não existe no catálogo.")
        return
    if cod_armazem not in estoque:
        print(f"Erro: Armazém '{cod_armazem}' não existe.")
        return
    if quantidade <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
        return

    # Lógica de Remoção
    armazem = estoque[cod_armazem]
    quantidade_atual = armazem.get(cod_produto, 0)
    nome_produto = produtos.get(cod_produto, "Desconhecido")
    nome_armazem = armazens.get(cod_armazem, "Desconhecido")

    if quantidade_atual < quantidade:
        print(f"Erro: Estoque insuficiente de '{nome_produto}' em '{nome_armazem}'.")
        print(f"  Disponível: {quantidade_atual} | Tentativa de remoção: {quantidade}")
    else:
        armazem[cod_produto] = quantidade_atual - quantidade
        print(f"Sucesso: Estoque de '{nome_produto}' atualizado para {armazem[cod_produto]} no armazém '{nome_armazem}'.")

def transferir_estoque(cod_produto, armazem_origem, armazem_destino, quantidade):
    """
    Movimenta o estoque de um armazém para outro (usando os códigos).
    """
    print(f"--- Tentando transferir {quantidade} un. de '{cod_produto}' de Cód '{armazem_origem}' para Cód '{armazem_destino}' ---")

    # Verificações
    if cod_produto not in produtos:
        print(f"Erro: Produto '{cod_produto}' não existe no catálogo.")
        return
    if armazem_origem not in estoque:
        print(f"Erro: Armazém de origem '{armazem_origem}' não existe.")
        return
    if armazem_destino not in estoque:
        print(f"Erro: Armazém de destino '{armazem_destino}' não existe.")
        return
    if quantidade <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
        return
    if armazem_origem == armazem_destino:
        print("Erro: O armazém de origem e destino não podem ser os mesmos.")
        return

    # 1. Verificar se há estoque suficiente na ORIGEM
    armazem = estoque[armazem_origem]
    quantidade_atual_origem = armazem.get(cod_produto, 0)
    nome_armazem_origem = armazens.get(armazem_origem, "Desconhecido")

    if quantidade_atual_origem < quantidade:
        print(f"Erro: Estoque insuficiente em '{nome_armazem_origem}' (Cód: {armazem_origem}).")
        print(f"  Disponível: {quantidade_atual_origem} | Tentativa de transferência: {quantidade}")
    else:
        # 2. Se tiver, remover da origem
        print(f"Removendo {quantidade} de '{nome_armazem_origem}'...")
        armazem[cod_produto] = quantidade_atual_origem - quantidade
        
        # 3. Adicionar no destino
        nome_armazem_destino = armazens.get(armazem_destino, "Desconhecido")
        print(f"Adicionando {quantidade} em '{nome_armazem_destino}'...")
        armazem_dest = estoque[armazem_destino]
        quantidade_atual_destino = armazem_dest.get(cod_produto, 0)
        armazem_dest[cod_produto] = quantidade_atual_destino + quantidade
        
        print("Sucesso: Transferência concluída.")

# -------------------------
# --- Funções de Exibição ---
# -------------------------

def visualizar_estoque_geral():
    """
    (ALTERADO) Mostra o estado completo dos 3 catálogos.
    """
    print("\n================================")
    print("      CATÁLOGO DE PRODUTOS")
    print("================================")
    if not produtos:
        print("Nenhum produto registado.")
    else:
        for cod, nome in produtos.items():
            print(f"Cód: {cod} | Nome: {nome}")
    
    print("\n================================")
    print("     CATÁLOGO DE ARMAZÉNS")
    print("================================")
    if not armazens:
        print("Nenhum armazém registado.")
    else:
        for cod, nome in armazens.items():
            print(f"Cód: {cod} | Nome: {nome}")

    print("\n================================")
    print("      ESTOQUE POR ARMAZÉM")
    print("================================")
    if not estoque:
        print("Nenhum armazém com estoque.")
    else:
        # Itera sobre o dicionário 'estoque'
        for cod_armazem, itens in estoque.items():
            
            # Consulta o nome do armazém no catálogo 'armazens'
            nome_armazem = armazens.get(cod_armazem, "[Armazém Desconhecido]")
            
            print(f"\n### Cód: {cod_armazem} - Armazém: {nome_armazem.upper()} ###")
            
            if not itens:
                print("  (Armazém vazio)")
            else:
                for cod_produto, quant in itens.items():
                    # Consulta o nome do produto no catálogo 'produtos'
                    nome_produto = produtos.get(cod_produto, f"[Produto {cod_produto} não encontrado]")
                    if quant > 0: # Só mostra se tiver estoque
                        print(f"  Cód: {cod_produto} | Produto: {nome_produto} | Quantidade: {quant}")
    print("================================\n")


def mostrar_menu():
    """Apenas imprime o menu de opções."""
    print("\n--- Sistema de Gestão de Estoque v3 ---")
    print("1. Criar novo produto (no catálogo)")
    print("2. Criar novo armazém")
    print("3. Adicionar estoque (Dar entrada)")
    print("4. Remover estoque (Dar saída)")
    print("5. Transferir estoque (Movimentar)")
    print("6. Visualizar estoque geral")
    print("0. Sair")

# --------------------------------
# --- Função Principal (O Menu) ---
# --------------------------------

def main():
    """
    Função principal que executa o menu interativo.
    """
    while True:
        mostrar_menu()
        
        opcao = input("Escolha uma opção: ").strip()

        print("-" * 30) # Linha divisória

        if opcao == "1":
            # --- Criar Produto ---
            cod = input("Digite o código do novo produto: ").strip()
            nome = input("Digite o nome do novo produto: ").strip()
            criar_produto(cod, nome)

        elif opcao == "2":
            # --- Criar Armazém (ALTERADO) ---
            cod_armazem = input("Digite o código do novo armazém (ex: 01): ").strip()
            nome_armazem = input("Digite o nome do novo armazém (ex: Armazem Principal): ").strip()
            criar_armazem(cod_armazem, nome_armazem)

        elif opcao == "3":
            # --- Adicionar Estoque ---
            try:
                cod_produto = input("Digite o código do produto: ").strip()
                cod_armazem = input("Digite o código do armazém de entrada: ").strip() # Não usamos mais .lower()
                quantidade = int(input("Digite a quantidade a adicionar: ").strip())
                adicionar_estoque(cod_produto, cod_armazem, quantidade)
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro.")

        elif opcao == "4":
            # --- Remover Estoque ---
            try:
                cod_produto = input("Digite o código do produto: ").strip()
                cod_armazem = input("Digite o código do armazém de saída: ").strip()
                quantidade = int(input("Digite a quantidade a remover: ").strip())
                remover_estoque(cod_produto, cod_armazem, quantidade)
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro.")

        elif opcao == "5":
            # --- Transferir Estoque ---
            try:
                cod_produto = input("Digite o código do produto: ").strip()
                armazem_origem = input("Digite o código do armazém de ORIGEM: ").strip()
                armazem_destino = input("Digite o código do armazém de DESTINO: ").strip()
                quantidade = int(input("Digite a quantidade a transferir: ").strip())
                transferir_estoque(cod_produto, armazem_origem, armazem_destino, quantidade)
            except ValueError:
                print("Erro: A quantidade deve ser um número inteiro.")

        elif opcao == "6":
            # --- Visualizar Estoque ---
            visualizar_estoque_geral()

        elif opcao == "0":
            # --- Sair ---
            print("Obrigado por usar o sistema. Até logo!")
            break
        
        else:
            print("Erro: Opção inválida. Tente novamente.")

# -----------------------------------------------------------------
# --- Ponto de Entrada: Executa a função 'main' quando o script é corrido ---
# -----------------------------------------------------------------
if __name__ == "__main__":
    # Vamos pré-criar produtos e armazéns para testes
    criar_produto("001", "Parafuso Sextavado")
    criar_produto("002", "Porca")
    
    criar_armazem("01", "Armazem Principal")
    criar_armazem("02", "Armazem Expedicao")
    
    # Vamos pré-adicionar algum estoque
    print("-" * 30)
    adicionar_estoque("001", "01", 100) # Adiciona 100 parafusos no armazém "01"
    adicionar_estoque("002", "01", 50)  # Adiciona 50 porcas no armazém "01"
    adicionar_estoque("001", "02", 10)  # Adiciona 10 parafusos na "Expedição"
    
    # Inicia o menu interativo
    main() 