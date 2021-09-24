#!/usr/local/bin/python
# coding: utf-8
#CARREGAMENTO

##################################################################################################################################################################
# Created on 22 de Julho de 2021
#
#     Projeto base: Cavaleiro dos Zodiacos
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

# carregando os arquivos


from transform import Transform
import pymongo
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('CVZ')
logger.setLevel(logging.DEBUG)

#conexao
for i in range(100):
    tabela = Transform(i).tabela
    client = pymongo.MongoClient("mongo", 27017)
    db = client['cavaleirodoszodiacos']
    collections = db['personagem']
    collections.insert_many(tabela.to_dict('records'))




logger.info("CARREGAMENTO DOS DADOS NO MONGODB")