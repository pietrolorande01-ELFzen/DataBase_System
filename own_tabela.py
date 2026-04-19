import pandas as pd # pandas é uma biblioteca de python que ajuda a trabalhar com dados, /PD é um apelido que jogamos nela quando colocamos o "as"

import random       # é um biblioteca que gera números aletórios para o programa

from datetime import datetime, timedelta        # Comandos que ajudam a trabalhar com horários




# lista de dados fictícios
# Neste momento em cada uma das listas que disponibilizamos estamos colocando dentro delas, várias "Nomeclaturas", que serão utilizados pelo "random" posteriormente para gerar a tabela 

cidades = ["São Paulo", "Belo Horizonte", "Manaus", "Rio de Janeiro", "Curitiba", "Bahia", "Salvador"]
status_pedido = ["Entregue", "Em transito", "Atrasado" , "Cancelado"]
tipos_de_entrega = ["Normal", "Express" , "Same Day"]
transportadoras = ["Correios", "Loggi", "Jadlog", "Total Express"]
produtos = ["Eletrônicos", "Roupas", "Alimentos", "Livros", "Móveis"] 

#Aqui(em cima) criamos toda a base de dados com os rótulos que vamos usar...todas as informações que vão constar na tabela

#vamos criar aqui a função de gerar datas aleatórias
def gerar_data():
    inicio = datetime(2026,1,1)     # Usamos a disposição de Year, Month, Day
    return inicio + timedelta(days=random.randint(0,365))


#No return estamos fazendo com que o timedelta gere um dia aletório e informe ele ao "inicio"

# Vamos criar a base de dados aletória agora

dados = []

for i in range(120):
    linha = {
        "ID_Pedido": i + 1,  # Agora o ID é numérico e sequencial (melhor para controle)
        "Cidade_Origem": random.choice(cidades),
        "Cidade_Destino": random.choice(cidades),

        "Tipo_de_Entrega": random.choice(tipos_de_entrega),
        "Transportadora": random.choice(transportadoras),
        "Categoria_de_Produto": random.choice(produtos),

        # round(random.uniform(0.5,50), 2 ) || o random.uniform usamos para gerar, um valor uniforme aleatório
        # para dar mais especificidade usamos, o (0.5, 50), para ser um número entre os dois (float)
        # Com isso o ",2" que vem em seguida vem trabalha com duas casas decimais em seu arredondamento

        "Peso_KG": round(random.uniform(0.5, 50) ,2),
        "Valor_R$": round(random.uniform(50, 5000) ,2),
        "Distancia_KM": random.randint(10, 3000),               # O uso do randit em si ele só gera um número aleatório mesmo, (Normal)
        "Tempo_Entrega_dias": random.randint(1, 15),            

        "Status": random.choice(status_pedido),
        "Data_pedido": gerar_data(),
        "Data_Entrega": gerar_data(),

        "Frete_R$": round(random.uniform(10,300) ,2),
        "Avaliação_Cliente": random.randint(1,5)

    }

    dados.append(linha)

#Vamos criar um DataFrame 

df = pd.DataFrame(dados)            #Aqui ele está convertendo os nossos dados em uma tabela tipica do pandas

# Vamos salvar o arquivo em formato de .XLSX

df.to_excel("Base_logistica.xlsx", index=False)

# df.to_csv("base_logistica.csv", index=False) || se quisermos salvar em .csv

# Aqui vamos fazer com que o progrma mostre as primeiras linhas.

print(df.head(100))

# No comando head(x) delimitamos quantas linhas queremos exibir




















































































































