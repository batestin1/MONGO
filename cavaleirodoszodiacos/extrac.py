#!/usr/local/bin/python
# coding: latin-1
#extra��o

##################################################################################################################################################################
# Created on 22 de Julho de 2021
#
#     Projeto base: Cavaleiro dos Zodiacos
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
#IMPORT

import requests
class Extrac():
    def __init__(self):
        self.persona = requests.get('https://saint-seiya-api.herokuapp.com/api/characters').json()
print('#'*60)
print('Seus dados est�o sendo EXTRAIDOS!')
print('#'*60)