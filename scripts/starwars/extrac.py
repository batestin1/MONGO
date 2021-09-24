#!/usr/local/bin/python
# coding: utf-8
#EXTRA��O

##################################################################################################################################################################
# Created on 13 de Julho de 2021
#
#     Projeto base: STAR WARS
#     Reposit�rio: MONGO
#     Cole��o: PESSOAS
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
# IMPORTS

import requests
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('STAR WARS')
logger.setLevel(logging.DEBUG)

class Extrac_peolpe():
    def __init__(self, i):
        self.dados = requests.get(f'https://swapi.dev/api/people/?page={i}').json()
class Extrac_planets():
    def __init__(self, i):
        self.dados = requests.get(f'https://swapi.dev/api/planets/?page={i}').json()
class Extrac_species():
    def __init__(self, i):
        self.dados = requests.get(f'https://swapi.dev/api/species/?page={i}').json()
class Extrac_starship():
    def __init__(self, i):
        self.dados = requests.get(f'https://swapi.dev/api/starships/?page={i}').json()
class Extrac_vehicles():
    def __init__(self, i):
        self.dados = requests.get(f'https://swapi.dev/api/vehicles/?page={i}').json()

logger.info("EXTRAÇÃO DOS DADOS DA API")

