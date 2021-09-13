#!/usr/local/bin/python
# coding: latin-1
#CARREGAMENTO

##################################################################################################################################################################
# Created on 22 de Julho de 2021
#
#     Projeto base: Cavaleiro dos Zodiacos
#     Repositório: MONGO
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################

# carregando os arquivos


from transform import Transform
import pymongo


#conexao
for i in range(100):
    tabela = Transform(i).tabela
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['cavaleirodoszodiacos']
    collections = db['personagem']
    collections.insert_many(tabela.to_dict('records'))




print('Seus dados foram CARREGADOS!')
print('#'*60)