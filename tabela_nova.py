import pandas as pd              # Biblioteca para manipulação e análise de dados
import random                    # Biblioteca para geração de valores aleatórios
from datetime import datetime, timedelta  # Manipulação de datas e intervalos de tempo

random.seed(42)  # Define uma semente fixa para garantir reprodutibilidade dos dados

# Listas base utilizadas para gerar dados aleatórios
cidades = ["São Paulo", "Belo Horizonte", "Manaus", "Rio de Janeiro", "Curitiba", "Salvador"]
status_pedido = ["Entregue", "Em trânsito", "Atrasado", "Cancelado"]
tipos_de_entrega = ["Normal", "Express", "Same Day"]
transportadoras = ["Correios", "Loggi", "Jadlog", "Total Express"]
produtos = ["Eletrônicos", "Roupas", "Alimentos", "Livros", "Móveis"]

# Função que gera uma data aleatória ao longo do ano de 2026
def gerar_data():
    inicio = datetime(2026, 1, 1)
    return inicio + timedelta(days=random.randint(0, 365))


dados = []  # Lista que armazenará todos os registros gerados

# Loop para gerar 120 pedidos simulados
for i in range(120):

    # Define cidade de origem e destino (garantindo que sejam diferentes)
    origem = random.choice(cidades)
    destino = random.choice([c for c in cidades if c != origem])

    # Geração de variáveis logísticas
    distancia = random.randint(10, 3000)              # Distância em km
    peso = round(random.uniform(0.5, 50), 2)          # Peso em kg

    # Cálculo do tempo de entrega baseado na distância (aproximação)
    tempo_entrega = max(1, int(distancia / 300))

    # Geração das datas de pedido e entrega
    data_pedido = gerar_data()
    data_entrega = data_pedido + timedelta(days=tempo_entrega)

    # Geração de valores financeiros
    valor = round(random.uniform(50, 5000), 2)        # Valor do pedido
    frete = round((distancia * 0.05) + (peso * 2), 2) # Cálculo do frete

    hoje = datetime.now()  # Data atual para comparação de status

    # Definição do status do pedido com base em regras de negócio
    if random.random() < 0.05:
        status = "cancelado"
        data_entrega = None  # Pedido cancelado não possui data de entrega
    elif data_entrega < hoje:
        status = "atrasado" if random.random() < 0.1 else "entregue"
    else:
        status = "em_transito"

    # Estruturação do pedido em formato de dicionário (linha da tabela)
    linha = {
        "id_pedido": i + 1,
        "cidade_origem": origem,
        "cidade_destino": destino,
        "tipo_entrega": random.choice(tipos_de_entrega).lower().replace(" ", "_"),
        "transportadora": random.choice(transportadoras).lower().replace(" ", "_"),
        "categoria_produto": random.choice(produtos).lower(),
        "peso_kg": peso,
        "valor_rs": valor,
        "distancia_km": distancia,
        "tempo_entrega_dias": tempo_entrega,
        "status": status,
        "data_pedido": data_pedido,
        "data_entrega": data_entrega,
        "frete_rs": frete,
        "avaliacao_cliente": random.randint(1, 5)  # Nota de satisfação do cliente
    }

    dados.append(linha)  # Adiciona o pedido à lista

# Criação do DataFrame a partir da lista de pedidos
df = pd.DataFrame(dados)

# Exportação da base para arquivo Excel (.xlsx)
df.to_excel("base_logistica_normalizada.xlsx", index=False)

# Exibe as primeiras 100 linhas para visualização no terminal
print(df.head(120))

















