import pandas as pd 
import numpy as np
from datetime import datetime #biblioteca que trabalha com tempo 
import matplotlib.pyplot as plt 
import os 
import polars as pl 

os.system('cls')

ENDERECO_DADOS = r'../dados/'

pasta = os.listdir(ENDERECO_DADOS)

try:
    print('Obtendo dados...')

    hora_inicial = datetime.now()
    
    df_bolsa_familia = None
    # for arquivo in lista_arquivos:
    #     print(f'\nProcessando o arquivo: {arquivo}')

    #     df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1')
        
    #     if df_bolsa_familia is None:
    #         df_bolsa_familia = df
    #     else:
    #         df_bolsa_familia = pd.concat([df_bolsa_familia, df])
        
    #     del df
        
    print('Obtendo dados...')

    hora_inicial = datetime.now()
    
    df_bolsa_familia = None

    for arquivo in pasta:
        print(f'\nProcessando o arquivo: {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
    
        del df

    hora_final = datetime.now()

    print(f'Tempo de execução: {hora_final - hora_inicial}')

except Exception as e:
    print(f'Erro ao realizar a leitura dos meses{e}')