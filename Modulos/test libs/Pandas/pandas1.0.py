import pandas as pd
from IPython.display import display

#criando difionario com as informações
venda = {
    'data': ['18/01/2005', '28/02/2005'],
    'valor': [500, 300],
    'produto': ['feijão', 'arroz'],
    'qtde': [50,70],
}

#criando um dataframe
vendas_df= pd.DataFrame(venda)

#visualização
#print(vendas_df)
#display(vendas_df)

#lendo o excel
vendas_df2= pd.read_excel("Vendas.xlsx")


pd.options.display.max_columns = None #----->habilitanto todas as colunas maximas para aparecer


#metodos para exebição da tabela

# print(vendas_df2.shape) -----> mostrar a quantidades de linhas
# display(vendas_df2.head(10)) -----> mostrar as 10 primeiras linhas
# display(vendas_df2.describe()) ----> mostrar a decrição ou resumo da tabela

# produtos = (vendas_df2.loc[1:4]) -----> mostrar as de 1 a 4
# ljnorte = vendas_df2[['ID Loja','Produto']] -----> criar uma variavel e receber, colunas

#procurar por informação na coluna
norte = vendas_df2.loc[vendas_df2['ID Loja']=='Norte Shopping']
#Procurar por linhas e colunas
venda_norte = vendas_df2.loc[vendas_df2['ID Loja']=='Norte Shopping', ['ID Loja','Produto','Quantidade']]

print(vendas_df2.loc[1,'Produto'])