#!/usr/local/bin/python
# coding: latin-1
#EXTRA��O

##################################################################################################################################################################
# Created on 13 de Julho de 2021
#
#     Projeto base: STAR WARS
#     Reposit�rio: MONGO
#     Cole��o: NAVES
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
# IMPORTS

import requests

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://swapi.dev/api/starships/?page={i}').json()

print('-'*60)
print('EXTRAIDOS, seus dados sendo est�o')
print('-'*60)

