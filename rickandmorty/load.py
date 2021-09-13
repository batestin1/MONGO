#!/usr/local/bin/python
# coding: latin-1
#CARREGAMENTO

##################################################################################################################################################################
# Created on 17 de Julho de 2021
#
#     Projeto base: RICK AND MORTY
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from transform import Transform
import pymongo




client = pymongo.MongoClient('127.0.0.1', 27017)

for b in range(20):
    tab = Transform(b).tab
    db = client['rickmorty']
    collections = db['personagem']
    collections.insert_many(tab.to_dict('records'))

print('Seus dados foram CARREGADOS!')
print('#'*60)