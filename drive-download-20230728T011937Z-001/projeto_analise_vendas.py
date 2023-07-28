# "os" eh uma biblioteca do python criada para tratar, manipular arquivos locais
# da propria maquina
import os
# "pandas" uma biblioteca do Python que o objetivo eh trabalhar com base de dados
# "as" eh um apelido que a gente atribui a um import / uma abreviacao
import pandas as pd
# importacao de biblioteca para criar grafico
import plotly.express as px

# guarda dentro desta variavel todos os arquivos que estao dentro do diretorio
lista_arquivo = os.listdir("C://Users/nsmar/OneDrive/Área de Trabalho/dev/Projeto Python - analise de vendas/drive-download-20230728T011937Z-001/Vendas")

# estou criando uma tabela vazia
tabela_total = pd.DataFrame()

# sintaxe "for" eh " for variavel in lista_de_algo"
for arquivo in lista_arquivo:
    if "vendas" in arquivo.upper() or "vendas" in arquivo.lower():
# "f" diz que o texto aceita formatacao de forma dinamica
# Importando base de dados lendo os arquivos e importando em uma tabela
        tabela_vendas = pd.read_csv(f"C://Users/nsmar/OneDrive/Área de Trabalho/dev/Projeto Python - analise de vendas/drive-download-20230728T011937Z-001/Vendas/{arquivo}")
        tabela_total = tabela_total._append(tabela_vendas)

print(tabela_total)

# Calcular produto mais vendido em (quantidade)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]]
print(tabela_produtos)


# Calcular produto que mais faturou
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]]
print(tabela_faturamento)

# Cacular a loja que mais vendeu em faturamento
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]]
print(tabela_lojas)

# Criacao de grafico
grafico_produtos = px.bar(tabela_produtos, x=tabela_produtos.index, y="Quantidade Vendida")
# Exibe o grafico
grafico_produtos.show()

grafico_lojas = px.area(tabela_lojas, x= tabela_lojas.index, y="Faturamento")
grafico_lojas.show()

