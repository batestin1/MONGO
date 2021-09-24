#!/usr/local/bin/python
# coding: utf-8
# TRANSFORM

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

from extrac import Extrac_peolpe, Extrac_planets, Extrac_species, Extrac_starship, Extrac_vehicles
import pandas as pd
import pymongo
import logging
import sys
# Configuracao de logs de aplicacao
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('STAR WARS')
logger.setLevel(logging.DEBUG)

client = pymongo.MongoClient('mongo', 27017)


class Transform_people():
    def __init__(self):
        for i in range(1,9):
            dados = Extrac_peolpe(i).dados
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
                       'Raca': [especie]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['pessoas']
                collections.insert_many(tabela.to_dict('records'))
class Transform_planets():
    def __init__(self):
        for i in range(1,6):
            dados = Extrac_planets(i).dados
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
                       'Periodo de Rotacao': [rotacao],
                       'Periodo Orbital': [orbita],
                       'Diametro': [diametro],
                       'Clima': [clima],
                       'Gravidade': [gravidade],
                       'Tipo de Terreno': [terreno],
                       'Populacao': [populacao],
                       'Residentes': [residents]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['planetas']
                collections.insert_many(tabela.to_dict('records'))
class Transform_species():
    def __init__(self):
        for i in range(1,4):
            dados = Extrac_species(i).dados
            for b in range(10):
                nome = dados['results'][b]['name']
                classificacao = dados['results'][b]['classification']
                designacao = dados['results'][b]['designation']
                altura = dados['results'][b]['average_height']
                expectativa = dados['results'][b]['average_lifespan']
                linguagem = dados['results'][b]['language']
                nacionalidade = dados['results'][b]['homeworld']
                tab = {'Nome': [nome],
                       'Classificacao': [classificacao],
                       'Designacao': [designacao],
                       'Altura': [altura],
                       'Expectativa de Vida': [expectativa],
                       'Linguagem': [linguagem],
                       'Nacionalidade': [nacionalidade]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['racas']
                collections.insert_many(tabela.to_dict('records'))
class Transform_starship():
    def __init__(self):
        for i in range(1,4):
            dados = Extrac_starship(i).dados
            for b in range(10):
                nome = dados['results'][b]['name']
                modelo = dados['results'][b]['model']
                classe = dados['results'][b]['starship_class']
                fabricante = dados['results'][b]['manufacturer']
                valor = dados['results'][b]['cost_in_credits']
                altura = dados['results'][b]['length']
                velocidade = dados['results'][b]['max_atmosphering_speed']
                equipe = dados['results'][b]['crew']
                passageiros = dados['results'][b]['passengers']
                carga = dados['results'][b]['cargo_capacity']
                combustivel = dados['results'][b]['consumables']
                hyperdrive = dados['results'][b]['hyperdrive_rating']
                piloto = dados['results'][b]['pilots']
                tab = {'Nome': [nome],
                       'Modelo': [modelo],
                       'classe': [classe],
                       'Fabricante': [fabricante],
                       'Valor no Mercado': [valor],
                       'Tamanho': [altura],
                       'Velocidade Planetaria': [velocidade],
                       'Total de Equipe': [equipe],
                       'Capacidade de Passageiros': [passageiros],
                       'Capacidade de Carga': [carga],
                       'Consumo de Combustivel':[combustivel],
                       'Velocidade Hiperespaco': [hyperdrive],
                       'Pilotos': [piloto]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['naves']
                collections.insert_many(tabela.to_dict('records'))

class Transform_vehicles():
    def __init__(self):
        for i in range(1,4):
            dados = Extrac_vehicles(i).dados
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
                       'Velocidade Planet�ria': [velocidade],
                       'Total de Equipe': [equipe],
                       'Capacidade de Passageiros': [passageiros],
                       'Capacidade de Carga': [carga],
                       'Consumo de Combustivel':[combustivel],
                       'Pilotos': [piloto]}
                self.tabela = pd.DataFrame(tab)
                tabela = pd.DataFrame(tab)
                db = client['starwars']
                collections = db['veiculos']
                collections.insert_many(tabela.to_dict('records'))




logger.info("PROCESSANDO E TRANSFORMANDO OS DADOS")
