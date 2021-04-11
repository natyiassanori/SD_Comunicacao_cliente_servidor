#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:27:27 2021

@author: estanislau
"""

import socket
import _thread as thread


class Servidor():

    def __init__(self):
        self.host = ''              
        self.port = 8080            
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.origem = (self.host, self.port)
        self.tcp.bind(self.origem)	
        self.tcp.listen(10)
        self.numArquivo = 1    
        
        
    def novoCliente(self, conexao, cliente):
        ipCliente, _ = cliente
        print('Cliente {0} conectado!'.format(cliente))
        
        arquivo = open('./Pasta_Servidor/Planilha_'+str(self.numArquivo)+'_cliente_'+str(ipCliente)+".csv",'wb') 
          
        while(True):
            recebeDados = conexao.recv(4096)
            if not recebeDados: break
            
            while(recebeDados):
                arquivo.write(recebeDados)
                recebeDados = conexao.recv(4096)
        
        arquivo.close()
        self.numArquivo += 1
        
        
    def main(self):
        try:
            print("Aguardando conexão...")
            while(True):
                conexao, cliente = self.tcp.accept()
                thread.start_new_thread(self.novoCliente,(conexao, cliente))
                     
        finally:
            print("Encerrando o servidor...")
            self.tcp.close()
            
            

if __name__ == '__main__':
	execute_app = Servidor()
	execute_app.main()