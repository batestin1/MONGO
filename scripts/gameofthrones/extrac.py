#!/usr/local/bin/python
# coding: utf-8
#EXTRAC

##################################################################################################################################################################
# Created on 19 de Julho de 2021
#
#     Projeto base: GOT
#     Repositï¿½rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

import requests
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('GAME OF THRONES')
logger.setLevel(logging.DEBUG)


class Extrac():
    def __init__(self, b):
        self.people = requests.get(f'https://anapioficeandfire.com/api/characters/{b}').json()


logger.info("EXTRAÃÃO DOS DADOS DA API")