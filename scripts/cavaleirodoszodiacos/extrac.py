#!/usr/local/bin/python
# coding: utf-8
#extra��o

##################################################################################################################################################################
# Created on 22 de Julho de 2021
#
#     Projeto base: Cavaleiro dos Zodiacos
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
#IMPORT

import requests
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('CVZ')
logger.setLevel(logging.DEBUG)

class Extrac():
    def __init__(self):
        self.persona = requests.get('https://saint-seiya-api.herokuapp.com/api/characters').json()

logger.info("EXTRAÇÃO DOS DADOS DA API")