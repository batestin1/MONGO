#!/usr/local/bin/python
# coding: latin-1
#EXTRA��O

##################################################################################################################################################################
# Created on 20 de Julho de 2021
#
#     Projeto base: FUTURAMA
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests

class Extrac():
    def __init__(self):
        self.dados = requests.get('http://futuramaapi.herokuapp.com/api/v2/characters').json()


print('#'*60)
print('Seus dados est�o sendo EXTRAIDOS!')
print('#'*60)