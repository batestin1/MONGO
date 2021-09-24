#!/usr/local/bin/python
# coding: utf-8
#CARREGAMENTO

##################################################################################################################################################################
# Created on 20 de Julho de 2021
#
#     Projeto base: FUTURAMA
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
logger = logging.getLogger('FUTURAMA')
logger.setLevel(logging.DEBUG)

class Transform():
    def __init__(self, i):
            dados = Extrac().dados
            nome = dados[i]["Name"]
            especie = dados[i]["Species"]
            idade = dados[i]["Age"]
            planeta = dados[i]["Planet"]
            profissao = dados[i]['Profession']
            status = dados[i]["Status"]
            self.futurama = {'Personagem': [nome],
                        'Idade': [idade],
                        'Raca': [especie],
                        'Planeta de Origem': [planeta],
                        'Profissao': [profissao],
                        'Situacao Atual': [status]}
            self.futurama = pd.DataFrame(self.futurama)

logger.info("PROCESSANDO E TRANSFORMANDO OS DADOS")