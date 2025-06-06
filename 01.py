import streamlit as st
import pandas as pd
import numpy as np


# Lista de nomes de colunas (pode ser personalizada)
nomes_colunas = ["Nome", "Idade", "Cidade", "País"]  # Nomes de y colunas

def gerar_tabela(x, colunas, y): # Recebe as quantidades das linhas, os nomes das colunas e a quantidade das colunas
    dados = []
    for i in range(x):  # para cada linha
        linha = [] # valor de cada linha
        for j in range(y):  # para cada coluna
            valor = f"{i},{j}"  # ou qualquer outro conteúdo
            linha.append(valor)
        dados.append(linha)
    df = pd.DataFrame(dados, columns=colunas)
    return df

# Exibindo no Streamlit
x = 5  # número de linhas
y = len(nomes_colunas) # numero de colunas
tabela = gerar_tabela(x, nomes_colunas, y)
st.dataframe(tabela)




# Colocar uma barra de filtros
# Colocar checkbox para quando click atualiza a tabela
# Atualizar a tabela visualmente
