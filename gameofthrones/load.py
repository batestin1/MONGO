#!/usr/local/bin/python
# coding: latin-1
#CARREGAMENTO

##################################################################################################################################################################
# Created on 19 de Julho de 2021
#
#     Projeto base: GOT
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################


import pymongo
from transform import Transform




client = pymongo.MongoClient('127.0.0.1', 27017)

for a in range(3000):
    persona = Transform(a).persona
    familia = Transform(a).familia
    db = client['gameofthrones']
    collections = db['personagem']
    collections.insert_many(persona.to_dict('records'))
    db = client['gameofthrones']
    collections = db['casas']
    collections.insert_many(familia.to_dict('records'))

print('Seus dados foram CARREGADOS com sucesso!')
print('#'*60)
