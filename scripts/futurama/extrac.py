#!/usr/local/bin/python
# coding: utf-8
#EXTRA��O

##################################################################################################################################################################
# Created on 20 de Julho de 2021
#
#     Projeto base: FUTURAMA
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
logger = logging.getLogger('FUTURAMA')
logger.setLevel(logging.DEBUG)

class Extrac():
    def __init__(self):
        self.dados = requests.get('http://futuramaapi.herokuapp.com/api/v2/characters').json()


logger.info("EXTRAÇÃO DOS DADOS DA API")