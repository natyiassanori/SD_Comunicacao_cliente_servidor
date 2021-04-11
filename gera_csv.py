#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:07:25 2021

@author: estanislau
"""

import csv
from random import *

class GeraCSV():
    
    def __init__(self):
        self.nomeArquivo = 'Plantilla horaria identificación polen.csv'
        self.dadosPlanil = [[' ', '0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24'],
                            ['Acer'],
                            ['Aesculus'],
                            ['Alnus'],
                            ['Amaranthaceae'],
                            ['Apiaceae'],
                            ['Artemisia'],
                            ['Asteraceae'],
                            ['Betula'],
                            ['Brassicaceae'],
                            ['Cannabis'],
                            ['Castanea'],
                            ['Casuarina'],
                            ['Cedrus'],
                            ['Corylus'],
                            ['Cupressaceae'],
                            ['Cyperaceae'],
                            ['Echium'],
                            ['Ericaceae'],
                            ['Fabaceae'],
                            ['Fraxinus'],
                            ['Helianthus'],
                            ['Juncaceae'],
                            ['Liguliflora'],
                            ['Ligustrum'],
                            ['Mercurialis'],
                            ['Morus'],
                            ['Myrtaceae'],
                            ['Olea'],
                            ['Oleaeceae'],
                            ['Palmae'],
                            ['Pinus'],
                            ['Plantago'],
                            ['Platanus'],
                            ['Poaceae'],
                            ['Populus'],
                            ['Quercus'],
                            ['Rosaceae'],
                            ['Rumex'],
                            ['Salix'],
                            ['Sambucus'],
                            ['Ulmus'],
                            ['Urticaceae'],
                            ['Urtica memb.'],
                            ['Indetermin.'],
                            ['TOTAL']]

    
        
    def geraDados(self, dados):
        for i, dado in enumerate(dados):
            if i > 0:
                for j in range(len(dados[0]) - 1):
                    dados[i].append(round(uniform(0,10), 6))  
        return dados
 
       
    def escreveDadosPlanilha(self, dados):
        with open(self.nomeArquivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados)
      
        
    def main(self):
        dados = self.geraDados(self.dadosPlanil)
        self.escreveDadosPlanilha(dados)
 
           
if __name__ == '__main__':
    app = GeraCSV()
    app.main()