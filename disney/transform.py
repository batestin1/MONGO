#!/usr/local/bin/python
# coding: latin-1
#TRANSFORMA��O

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: DISNEY
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################


import pandas as pd
from extrac import Extrac


class Transform():
    def __init__(self, var):
        try:
            for i in range(1, 149):
                dados = Extrac(i).dados
                nome = dados['data'][var]['name']
                filme = dados['data'][var]['films'][0]
                shows = dados['data'][var]['tvShows'][0]
                allies = dados['data'][var]['allies'][0]
                enemies = dados['data'][var]['enemies'][0]
                disney = {'Nome': [nome],
                               'Filmes': [filme],
                               'TV Shows(S�ries)': [shows],
                               'Aliados': [allies],
                               'Inimigos': [enemies]}

                self.tab = pd.DataFrame(disney)



        except:
            for i in range(1, 149):
                dados = Extrac(i).dados
                nome = dados['data'][var]['name']
                filme = dados['data'][var]['films']
                shows = dados['data'][var]['tvShows']
                allies = dados['data'][var]['allies']
                enemies = dados['data'][var]['enemies']
                imagem = dados['data'][var]['sourceUrl']
                disney = {'Nome': [nome],
                               'Filmes': [filme],
                               'TV Shows(S�ries)': [shows],
                               'Aliados': [allies],
                               'Inimigos': [enemies],
                               'Info Original': [imagem]}

                self.tab = pd.DataFrame(disney)


print('Seus dados est�o sendo TRANSFORMADOS!')
print('#'*60)
