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


from transform import Transform
import pandas as pd
import pymongo


client = pymongo.MongoClient('127.0.0.1', 27017)

def main():

    for i in range(20):
        futurama = Transform(i).futurama
        db = client['futurama']
        collections = db['personagem']
        futurama = pd.DataFrame(futurama)
        collections.insert_many(futurama.to_dict('records'))

if __name__ == '__main__':
    main()

print('Seus dados foram GRAVADOS com sucesso!')
print('#'*60)