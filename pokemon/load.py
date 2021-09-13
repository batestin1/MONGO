#!/usr/local/bin/python
# coding: latin-1
#TRANSFORMAÇÃO

##################################################################################################################################################################
# Created on 18 de Julho de 2021
#
#     Projeto base: POKEMON
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from pymongo import MongoClient
from transform import Transform

import pandas as pd
from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint

client = pymongo.MongoClient('127.0.0.1', 27017)


#conexao
b=0
for b in range(151):
    b = b+1
    pokedex = Transform(b).tab
    db = client['pokemon']
    collections = db['pokedex']
    collections.insert_many(pokedex.to_dict('records'))



print('*'* 100)
print('Seus dados foram CARREGADOS com sucesso!')