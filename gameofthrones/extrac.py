#!/usr/local/bin/python
# coding: latin-1
#EXTRAC

##################################################################################################################################################################
# Created on 19 de Julho de 2021
#
#     Projeto base: GOT
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests


class Extrac():
    def __init__(self, b):
        self.people = requests.get(f'https://anapioficeandfire.com/api/characters/{b}').json()
        self.casa = requests.get(f'https://www.anapioficeandfire.com/api/houses/{b}').json()
print('#'*60)
print('Seus dados est�o sendo EXTRAIDOS!')
print('#'*60)