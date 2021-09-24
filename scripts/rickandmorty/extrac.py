#!/usr/local/bin/python
# coding: utf-8
#EXTRA��O

##################################################################################################################################################################
# Created on 17 de Julho de 2021
#
#     Projeto base: RICK AND MORTY
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
logger = logging.getLogger('RICK AND MORTY')
logger.setLevel(logging.DEBUG)

class Extrac():
    def __init__(self, i):
        self.dados = requests.get(f'https://rickandmortyapi.com/api/character?page={i}').json()
        
logger.info("EXTRAÇÃO DOS DADOS DA API")