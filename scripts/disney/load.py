#!/usr/local/bin/python
# coding: utf-8
#CARREGAMENTO

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: DISNEY
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from pymongo import MongoClient
from transform import Transform
import pymongo

import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('DISNEY')
logger.setLevel(logging.DEBUG)


for var in range(0, 49):
    disney = Transform(var).tab
    client = pymongo.MongoClient('mongo', 27017)
    db = client['DISNEY']
    collections = db['PERSONAGEM']
    collections.insert_many(disney.to_dict('records'))


logger.info("CARREGANDO OS DADOS NO MONGODB")
