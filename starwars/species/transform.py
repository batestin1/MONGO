#!/usr/local/bin/python
# coding: latin-1
# TRANSFORM

##################################################################################################################################################################
# Created on 13 de Julho de 2021
#
#     Projeto base: STAR WARS
#     Repositório: MONGO
#     Coleção: ESPECIES
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
        for i in range(1,4):
            dados = Extrac(i).dados
            for b in range(10):
                nome = dados['results'][b]['name']
                classificacao = dados['results'][b]['classification']
                designacao = dados['results'][b]['designation']
                altura = dados['results'][b]['average_height']
                expectativa = dados['results'][b]['average_lifespan']
                linguagem = dados['results'][b]['language']
                nacionalidade = dados['results'][b]['homeworld']
                tab = {'Nome': [nome],
                       'Classificação': [classificacao],
                       'Designação': [designacao],
                       'Altura': [altura],
                       'Expectativa de Vida': [expectativa],
                       'Linguagem': [linguagem],
                       'Nacionalidade': [nacionalidade]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['racas']
                collections.insert_many(tabela.to_dict('records'))







print('TRANSFORMADOS, seus dados sendo estão')
print('-'*60)

