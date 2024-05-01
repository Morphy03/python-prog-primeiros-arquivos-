# Logica de progrramação
#Passo 0 - Entender oq qr resolver

#Passo 1 - Percorrer todos os arquivos da pasta vendas
import os 
import pandas as pd
import plotly.express as px

lista_arq = os.listdir('/content/drive/MyDrive/Python colab/Vendas')
print(lista_arq)

tabela_total = pd.DataFrame()

#Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arq:
    if 'Vendas' in arquivo:
        tabela = pd.read_csv(f'/content/drive/MyDrive/Python colab/Vendas/{arquivo}')
        tabela_total = tabela_total.append(tabela)
#Passo 3 - compilar as bases de dados
print(tabela_total)

#Passo 4 - Calcular o produto mais vendido(quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum() 
tabela_produtos = tabela_produtos[['Quantidade Vendida', ]].sort_values(by='Quantidade Vendida', ascending=False) 
print(tabela_produtos)

#Passo 5 - Calcular o produto mais faturado
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
#criar nova coluna
tabela_faturamento = tabela_total.groupby('Produto').sum() 
tabela_faturamento = tabela_faturamento[['Faturamento', ]].sort_values(by='Faturamento', ascending=False) 
print(tabela_faturamento)

#Passo 6 - Calcular loja/cidade q mais vendeu(faturamento) - criar grafico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum() 
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()