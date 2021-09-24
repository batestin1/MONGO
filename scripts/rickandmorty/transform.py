#!/usr/local/bin/python
# coding: utf-8
#TRANSFORMA��O

##################################################################################################################################################################
# Created on 17 de Julho de 2021
#
#     Projeto base: RICK AND MORTY
#     Reposit�rio: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from extrac import Extrac
import pandas as pd
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('RICK AND MORTY')
logger.setLevel(logging.DEBUG)

class Transform():
    def __init__(self, b):
        for i in range(34):
            dados = Extrac(i).dados

        nome = dados['results'][b]['name']
        status = dados['results'][b]['status']
        specie = dados['results'][b]['species']
        gender = dados['results'][b]['gender']
        origin = dados['results'][b]['origin']['name']

        tabela = {'Nome': [nome],
                       'Genero': [gender],
                       'Condicao': [status],
                       'Especie': [specie],
                       'Planeta Natal': [origin]
                       }

        self.tab = pd.DataFrame(tabela)
logger.info("PROCESSANDO E TRANSFORMANDO OS DADOS")