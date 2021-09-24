#!/usr/local/bin/python
# coding: utf-8
#TRANSFORMA��O

##################################################################################################################################################################
# Created on 18 de Julho de 2021
#
#     Projeto base: POKEMON
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from pymongo import MongoClient
from transform import Transform
import pandas as pd
import pymongo
import pprint
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('POKEMON')
logger.setLevel(logging.DEBUG)

client = pymongo.MongoClient('mongo', 27017)


#conexao
b=0
for b in range(151):
    b = b+1
    pokedex = Transform(b).tab
    db = client['pokemon']
    collections = db['pokedex']
    collections.insert_many(pokedex.to_dict('records'))


logger.info("CARREGANDO OS DADOS NO MONGODB")