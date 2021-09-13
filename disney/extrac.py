#!/usr/local/bin/python
# coding: latin-1
#EXTRAÇÃO

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: DISNEY
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://api.disneyapi.dev/characters?page={i}').json()

print('#'*60)
print('Seus dados estão sendo EXTRAIDOS!')
print('#'*60)