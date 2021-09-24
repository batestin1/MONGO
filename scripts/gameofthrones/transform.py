#!/usr/local/bin/python
#  coding: utf-8
#TRANSFORMAï¿½ï¿½O

##################################################################################################################################################################
# Created on 19 de Julho de 2021
#
#     Projeto base: GOT
#     Repositï¿½rio: MONGO
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
logger = logging.getLogger('GAME OF THRONES')
logger.setLevel(logging.DEBUG)


class Transform():
    def __init__(self, a):

        b = 0
        for b in range(100):
            b = b + 1
            people = Extrac(b).people
            name = people['name']
            apelido = people['aliases']
            titulo = people['titles']
            genero = people['gender']
            culture = people['culture']
            born = people['born']
            url = people['url']

            # construindo os personagens

            self.persona = {'Nome Completo': [name],
                       'Cultura': [culture],
                       'Titulo Oficial': [titulo],
                       'Apelidos': [apelido],
                       'Genero': [genero],
                       'Ano de Nascimento': [born],
                       'Identificador': [url]}
            self.persona = pd.DataFrame(self.persona)






logger.info("PROCESSANDO E TRANSFORMANDO OS DADOS")