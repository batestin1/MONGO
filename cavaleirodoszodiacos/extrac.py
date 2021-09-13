#!/usr/local/bin/python
# coding: latin-1
#extração

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

import requests
class Extrac():
    def __init__(self):
        self.persona = requests.get('https://saint-seiya-api.herokuapp.com/api/characters').json()
print('#'*60)
print('Seus dados estão sendo EXTRAIDOS!')
print('#'*60)