#!/usr/local/bin/python
# coding: latin-1

#transformação

##################################################################################################################################################################
# Created on 22 de Julho de 2021
#
#     Projeto base: Cavaleiro dos Zodiacos
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
#IMPORT

from extrac import Extrac
import pandas as pd

class Transform():
    def __init__(self, i):
            persona = Extrac().persona
            nome = persona[i]['name']
            idade = persona[i]['age']
            nacionalidade = persona[i]['nationality']
            treinamento = persona[i]['training']
            altura = persona[i]['height']
            peso = persona[i]['weight']
            ataque = persona[i]['attacks']

            self.tabela = {
                'Nome': [nome],
                'Idade': [idade],
                'Nacionalidade': [nacionalidade],
                'Treinamento': [treinamento],
                'Altura': [altura],
                'Peso': [peso],
                'Ataque': [ataque]
            }
            self.tabela = pd.DataFrame(self.tabela)

print('Seus dados estão sendo TRANSFORMADOS!')
print('#'*60)