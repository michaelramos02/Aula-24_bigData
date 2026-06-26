import pandas as pd 
import numpy as np
from datetime import datetime #biblioteca que trabalha com tempo 
import matplotlib.pyplot as plt 
import os 
import polars as pl 

os.system('cls')


# Lendo Bolsa Familia 
try:
    ENDERECO_DADOS = r'../dados/'

    hora_inicial = datetime.now()

    print('Carregando...')

    #PANDAS 
    # df_janeiro = pd.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')


    #POLARS 00.00.06 É UMA BILIOTECA QUE TRABALHA COM MULTHREAD. POR ISSO RECOMENDASE P TRABLHO EM LARGA ESCALA, A TENDENCIA É QUE SEJA MAIS RAPIDO QUE O PANATAS POIS O PROCESSAMENTO DE DADOS É FEITO EM PARALELO
    #http://polaers.io
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_janeiro.head()) 
    print(df_janeiro.columns) #columns.to_list()
    print(df_janeiro.shape) # LINHAS E COLUNAS

    hora_final = datetime.now()

    print(f'Tempo de execução: {hora_final - hora_inicial}')

except Exception as e:
    print(f'Erro ao processar as informações {e}')