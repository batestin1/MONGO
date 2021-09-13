#!/usr/local/bin/python
# coding: latin-1
#EXTRAÇÃO

##################################################################################################################################################################
# Created on 20 de Julho de 2021
#
#     Projeto base: FUTURAMA
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests

class Extrac():
    def __init__(self):
        self.dados = requests.get('http://futuramaapi.herokuapp.com/api/v2/characters').json()


print('#'*60)
print('Seus dados estão sendo EXTRAIDOS!')
print('#'*60)