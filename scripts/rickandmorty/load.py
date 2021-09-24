#!/usr/local/bin/python
# coding: utf-8
#CARREGAMENTO

##################################################################################################################################################################
# Created on 17 de Julho de 2021
#
#     Projeto base: RICK AND MORTY
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from transform import Transform
import pymongo
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('RICK AND MORTY')
logger.setLevel(logging.DEBUG)



client = pymongo.MongoClient('mongo', 27017)

for b in range(20):
    tab = Transform(b).tab
    db = client['rickmorty']
    collections = db['personagem']
    collections.insert_many(tab.to_dict('records'))

logger.info("CARREGANDO OS DADOS NO MONGODB")