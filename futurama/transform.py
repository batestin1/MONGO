#!/usr/local/bin/python
# coding: latin-1
#CARREGAMENTO

##################################################################################################################################################################
# Created on 20 de Julho de 2021
#
#     Projeto base: FUTURAMA
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

from extrac import Extrac
import pandas as pd

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
                        'Raça': [especie],
                        'Planeta de Origem': [planeta],
                        'Profissão': [profissao],
                        'Situação Atual': [status]}
            self.futurama = pd.DataFrame(self.futurama)

print('Seus dados estão sendo TRANSFORMADOS!')
print('#'*60)