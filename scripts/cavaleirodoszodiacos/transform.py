#!/usr/local/bin/python
# coding: utf-8

#transforma��o

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

from extrac import Extrac
import pandas as pd
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('CVZ')
logger.setLevel(logging.DEBUG)

class Transform():
    def __init__(self, i):
            persona = Extrac().persona
            nome = persona[i]['name']
            idade = persona[i]['age']
            nacionalidade = persona[i]['nationality']
            treinamento = persona[i]['training']
            altura = persona[i]['height']
            peso = persona[i]['weight']
            ataque = persona[i]['attacks']

            self.tabela = {
                'Nome': [nome],
                'Idade': [idade],
                'Nacionalidade': [nacionalidade],
                'Treinamento': [treinamento],
                'Altura': [altura],
                'Peso': [peso],
                'Ataque': [ataque]
            }
            self.tabela = pd.DataFrame(self.tabela)

logger.info("CARREGAMENTO DOS DADOS NO MONGODB")