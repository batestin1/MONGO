#!/usr/local/bin/python
# coding: latin-1
# TRANSFORM

##################################################################################################################################################################
# Created on 13 de Julho de 2021
#
#     Projeto base: STAR WARS
#     Repositório: MONGO
#     Coleção: VEÍCULOS
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
        for i in range(1,4):
            dados = Extrac(i).dados
            for b in range(10):
                nome = dados['results'][b]['name']
                modelo = dados['results'][b]['model']
                classe = dados['results'][b]['vehicle_class']
                fabricante = dados['results'][b]['manufacturer']
                valor = dados['results'][b]['cost_in_credits']
                altura = dados['results'][b]['length']
                velocidade = dados['results'][b]['max_atmosphering_speed']
                equipe = dados['results'][b]['crew']
                passageiros = dados['results'][b]['passengers']
                carga = dados['results'][b]['cargo_capacity']
                combustivel = dados['results'][b]['consumables']
                piloto = dados['results'][b]['pilots']
                tab = {'Nome': [nome],
                       'Modelo': [modelo],
                       'classe': [classe],
                       'Fabricante': [fabricante],
                       'Valor no Mercado': [valor],
                       'Tamanho': [altura],
                       'Velocidade Planetária': [velocidade],
                       'Total de Equipe': [equipe],
                       'Capacidade de Passageiros': [passageiros],
                       'Capacidade de Carga': [carga],
                       'Consumo de Combustível':[combustivel],
                       'Pilotos': [piloto]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['veiculos']
                collections.insert_many(tabela.to_dict('records'))







print('TRANSFORMADOS, seus dados sendo estão')
print('-'*60)

