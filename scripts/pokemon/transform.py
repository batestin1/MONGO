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

from extrac import Extrac
import pandas as pd
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('POKEMON')
logger.setLevel(logging.DEBUG)

class Transform():
    def __init__(self, b):
        for i in range(1, 151):
            dados = Extrac(b).dados
            nome = dados['forms'][0]['name']
            peso = dados['weight']
            altura = dados['height']
            pokedex = dados['game_indices'][3]['game_index']
            tipo = dados['types'][0]['type']['name']
            habilidades = dados['abilities'][0]['ability']['name']
            ataque = dados['stats'][1]['base_stat']
            defesa = dados['stats'][2]['base_stat']

            pokedex = {'Pokemon': [nome],
                       'Tipo': [tipo],
                       'Pokedex': [pokedex],
                       'Altura': [altura],
                       'Peso': [peso],
                       'Habilidade': [habilidades],
                       'Ataque(hp)': [ataque],
                       'Defesa(hp)': [defesa]}
            self.tab = pd.DataFrame(pokedex)


logger.info("PROCESSANDO E TRANSFORMANDO OS DADOS")