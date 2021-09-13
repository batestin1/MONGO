#!/usr/local/bin/python
# coding: latin-1
#TRANSFORMAÇÃO

##################################################################################################################################################################
# Created on 17 de Julho de 2021
#
#     Projeto base: RICK AND MORTY
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from extrac import Extrac
import pandas as pd

class Transform():
    def __init__(self, b):
        for i in range(34):
            dados = Extrac(i).dados

        nome = dados['results'][b]['name']
        status = dados['results'][b]['status']
        specie = dados['results'][b]['species']
        gender = dados['results'][b]['gender']
        origin = dados['results'][b]['origin']['name']

        tabela = {'Nome': [nome],
                       'Genero': [gender],
                       'Condição': [status],
                       'Espécie': [specie],
                       'Planeta Natal': [origin]
                       }

        self.tab = pd.DataFrame(tabela)
print('#'*60)
print('Seus dados estão sendo TRANSFORMADOS')
