#!/usr/local/bin/python
# coding: latin-1
# TRANSFORM

##################################################################################################################################################################
# Created on 13 de Julho de 2021
#
#     Projeto base: STAR WARS
#     Repositório: MONGO
#     Coleção: PESSOAS
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
# IMPORTS

from extrac import Extrac
import pandas as pd
import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)


class Transform():
    def __init__(self):
        for i in range(1,9):
            dados = Extrac(i).dados
            for b in range(10):
                nome = dados['results'][b]['name']
                altura = dados['results'][b]['height']
                peso = dados['results'][b]['mass']
                cabelo = dados['results'][b]['hair_color']
                olhos = dados['results'][b]['eye_color']
                genero = dados['results'][b]['gender']
                especie = dados['results'][b]['species']
                tab = {'Nome': [nome],
                       'Altura': [altura],
                       'Peso': [peso],
                       'Cor do Cabelo': [cabelo],
                       'Cor dos Olhos': [olhos],
                       'Genero': [genero],
                       'Raça': [especie]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['pessoas']
                collections.insert_many(tabela.to_dict('records'))







print('TRANSFORMADOS, seus dados sendo estão')
print('-'*60)

