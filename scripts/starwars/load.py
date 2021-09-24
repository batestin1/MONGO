#!/usr/local/bin/python
# coding: utf-8
# LOAD

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
from transform import Transform_people, Transform_species, Transform_planets, Transform_starship, Transform_vehicles
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('STAR WARS')
logger.setLevel(logging.DEBUG)

#EXECUTANDO OS SCRIPTS

Transform_people()
Transform_species()
Transform_planets()
Transform_starship()
Transform_vehicles()


logger.info("CARREGANDO OS DADOS NO MONGODB")
