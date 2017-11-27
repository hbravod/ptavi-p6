#!/usr/binver/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
#Quitar el while y pasar la línea a lista con split
    def handle(self):       
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion \r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            lista = ['INVITE', 'ACK', 'BYE']
            print('El cliente envía:' + line.decode('utf-8'))
            method = ((line.decode('utf-8')).split(' ')[0])
            if not line:
                break
            if method == lista[0]:
                self.wfile.write(b"SIP/2.0 100 Trying \r\n"+
                                  b"SIP/2.0 180 Ringing \r\n"+
                                  b"SIP/2.0 200 OK \r\n")
            #envía canción
            elif method == lista[1]:
                pass
            elif method == lista[2]:
                elf.wfile.write(b"SIP/2.0 200 OK \r\n")
            elif method not in lista:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed \r\n")
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request \r\n")
            # Si no hay más líneas salimos del bucle infinito

if __name__ == "__main__":
    #Falta comprobar que existe el audio_file con os.path(?)
    if len(sys.argv) < 3:
        print("Usage: python3 server.py IP port audio_file")
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
