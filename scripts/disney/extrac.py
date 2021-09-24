#!/usr/local/bin/python
# coding: utf-8
#EXTRA��O

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: DISNEY
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('DISNEY')
logger.setLevel(logging.DEBUG)

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://api.disneyapi.dev/characters?page={i}').json()

logger.info("EXTRAÇÃO DOS DADOS DA API")