#!/usr/local/bin/python
# coding: latin-1
#TRANSFORMAÇÃO

##################################################################################################################################################################
# Created on 19 de Julho de 2021
#
#     Projeto base: GOT
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from extrac import Extrac
import pandas as pd

class Transform():
    def __init__(self, a):

        b = 0
        for b in range(1507):
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

        for b in range(443):
            b = b + 1

            casa = Extrac(b).casa
            house = casa['name']
            regiao = casa['region']
            armas = casa['ancestralWeapons']
            brasao = casa['coatOfArms']
            words = casa['words']
            senhor = casa['currentLord']
            fundado = casa['founded']
            membros = casa['swornMembers']

            # construindo as casas
            self.familia = {'CASA': [house],
                       'REGIÃO': [regiao],
                       'ARMAS ANCENTRAIS': [armas],
                       'BRASÃO': [brasao],
                       'LEMA': [words],
                       'SENHOR(a)': [senhor],
                       'FUNDADO POR': [fundado],
                       'MEMBROS': [membros]}

            self.familia = pd.DataFrame(self.familia)


print('Seus dados estão sendo TRANSFORMADOS!')
print('#'*60)
