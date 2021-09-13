#!/usr/local/bin/python
# coding: latin-1
# TRANSFORM

##################################################################################################################################################################
# Created on 13 de Julho de 2021
#
#     Projeto base: STAR WARS
#     Repositório: MONGO
#     Coleção: PLANETAS
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
# IMPORTS
from extrac import Extrac
import pandas as pd
import pymongo
from sshtunnel import SSHTunnelForwarder


client = pymongo.MongoClient('127.0.0.1', 27017)


class Transform():
    def __init__(self):
        for i in range(1,6):
            dados = Extrac(i).dados
            for b in range(10):
                nome = dados['results'][b]['name']
                rotacao = dados['results'][b]['rotation_period']
                orbita = dados['results'][b]['orbital_period']
                diametro = dados['results'][b]['diameter']
                clima = dados['results'][b]['climate']
                gravidade = dados['results'][b]['gravity']
                terreno = dados['results'][b]['terrain']
                populacao = dados['results'][b]['population']
                residents = dados['results'][b]['residents']
                tab = {'Nome': [nome],
                       'Periodo de Rotação': [rotacao],
                       'Periodo Orbital': [orbita],
                       'Diametro': [diametro],
                       'Clima': [clima],
                       'Gravidade': [gravidade],
                       'Tipo de Terreno': [terreno],
                       'População': [populacao],
                       'Residentes': [residents]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['planetas']
                collections.insert_many(tabela.to_dict('records'))







print('TRANSFORMADOS, seus dados sendo estão')
print('-'*60)

