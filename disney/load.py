#!/usr/local/bin/python
# coding: latin-1
#CARREGAMENTO

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: DISNEY
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from pymongo import MongoClient
from transform import Transform
import pymongo


for var in range(0, 49):
    disney = Transform(var).tab
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['DISNEY']
    collections = db['PERSONAGEM']
    collections.insert_many(disney.to_dict('records'))




print('Seus dados foram CARREGADOS com sucesso!')
print('#'*60)