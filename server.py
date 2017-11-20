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
        lista = ['INVITE', 'ACK', 'BYE']        
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion \r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            method = ((line.decode('utf-8')).split(' ')[0])
            print(line.decode('utf-8'))

            if method == 'INVITE':
                self.wfile.write(b"SIP/2.0 100 Trying \r\n"+
                                  b"SIP/2.0 180 Ringing \r\n"+
                                  b"SIP/2.0 200 OK \r\n")
            #envía canción
            elif method == 'ACK':
                pass
            elif method == 'BYE':
                elf.wfile.write(b"SIP/2.0 200 OK \r\n")
            if method in self.lista != 'INVITE' or method != 'ACK' or method != 'BYE':
                self.wfile.write(b"SIP/2.0 400 Bad Request \r\n")
            else:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed \r\n")
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    #Falta comprobar que existe el audio_file con os.path(?)
    if len(sys.argv) < 3:
        print("Usage: python3 server.py IP port audio_file")
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
