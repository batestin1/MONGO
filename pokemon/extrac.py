#!/usr/local/bin/python
# coding: latin-1
#TRANSFORMA��O

##################################################################################################################################################################
# Created on 18 de Julho de 2021
#
#     Projeto base: POKEMON
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()

print('*'* 100)
print('Seus dados est�o sendo EXTRAIDOS!')