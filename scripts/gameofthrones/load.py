#!/usr/local/bin/python
#  coding: utf-8
#CARREGAMENTO

##################################################################################################################################################################
# Created on 19 de Julho de 2021
#
#     Projeto base: GOT
#     Repositï¿½rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################


import pymongo
from transform import Transform
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('GAME OF THRONES')
logger.setLevel(logging.DEBUG)




for a in range(100):
    client = pymongo.MongoClient('mongo', 27017)
    persona = Transform(a).persona

    db = client['gameofthrones']
    collections = db['personagem']
    collections.insert_many(persona.to_dict('records'))


logger.info("CARREGANDO OS DADOS NO MONGODB")