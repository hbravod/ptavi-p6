#!/usr/binver/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import os
import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def error(line):
        line_errores = line.split(' ')
        if len(line_errores) != 3:
            fallo = True
        if line_errores[0] != 'sip':
            fallo = True
        if line_errores[1].find('@') == -1:
            fallo = True
        if line_errores[1].find(':') == -1:
            fallo = True
        if line_errores[2] != 'SIP/2.0\r\n\r\n':
            fallo = True
        return fallo

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
            if :
                self.wfile.write(b"SIP/2.0 400 Bad Request \r\n\r\n")
            if method == lista[0]:
                self.wfile.write(b"SIP/2.0 100 Trying \r\n\r\n"+
                                 b"SIP/2.0 180 Ringing \r\n\r\n"+
                                 b"SIP/2.0 200 OK \r\n\r\n")
            #envía canción
            elif method == lista[1]:
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + sys.argv[3]
                print("Vamos a ejecutar", aEjecutar)
                os.system(aEjecutar)
            elif method == lista[2]:
                self.wfile.write(b"SIP/2.0 200 OK \r\n\r\n")
            elif method not in lista:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed \r\n\r\n")
            # Si no hay más líneas salimos del bucle infinito

if __name__ == "__main__":
    #Falta comprobar que existe el audio_file con os.path(?)
    if len(sys.argv) < 3:
        print("Usage: python3 server.py IP port audio_file")
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening...")
    serv.serve_forever()
