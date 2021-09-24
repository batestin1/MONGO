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

import requests
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('POKEMON')
logger.setLevel(logging.DEBUG)

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()

logger.info("EXTRAÇÃO DOS DADOS DA API")