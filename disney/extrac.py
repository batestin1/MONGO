#!/usr/local/bin/python
# coding: latin-1
#EXTRA��O

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: DISNEY
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://api.disneyapi.dev/characters?page={i}').json()

print('#'*60)
print('Seus dados est�o sendo EXTRAIDOS!')
print('#'*60)