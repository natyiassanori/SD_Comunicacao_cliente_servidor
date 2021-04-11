#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:59:57 2021

@author: estanislau
"""

import socket
import glob
import time


class Cliente():

    def __init__(self):
        self.host = '192.168.0.6'              
        self.port = 8080            
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.destino = (self.host, self.port)
        self.tcp.connect(self.destino)    
        self.caminhoArquivos = './Pasta_Arquivos/*.csv'
        self.quantidadeArquivos = len((glob.glob(self.caminhoArquivos)))

    def main(self):
        print("Quantidade de arquivos a serem transferidos: {0}".format(self.quantidadeArquivos))
        for i in sorted(glob.glob(self.caminhoArquivos)):     
            print(i)
            
            arquivo = open(i, "rb")
            dados = arquivo.read(4096)
            while(dados):
                self.tcp.send(dados)
                dados = arquivo.read(4096)
                time.sleep(2)
                

        self.tcp.close() 

if __name__ == '__main__':
    execute_app = Cliente()
    execute_app.main()
