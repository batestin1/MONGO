#!/usr/local/bin/python
# coding: utf-8
#CARREGAMENTO

##################################################################################################################################################################
# Created on 20 de Julho de 2021
#
#     Projeto base: FUTURAMA
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################


from transform import Transform
import pandas as pd
import pymongo
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('FUTURAMA')
logger.setLevel(logging.DEBUG)


client = pymongo.MongoClient('mongo', 27017)

def main():

    for i in range(20):
        futurama = Transform(i).futurama
        db = client['futurama']
        collections = db['personagem']
        futurama = pd.DataFrame(futurama)
        collections.insert_many(futurama.to_dict('records'))

if __name__ == '__main__':
    main()

logger.info("CARREGANDO OS DADOS NO MONGODB")
