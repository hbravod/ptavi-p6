#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys


if len(sys.argv) < 3:
    print("Usage: python3 client.py method receiver@IP:SIPport")

# Cliente UDP simple.

# Contenido que vamos a enviar
LINE = sys.argv[2]

# Dirección IP del servidor.
SERVER = LINE.split('@')[1].split(':')[0]
PORT = int(LINE.split('@')[1].split(':')[1])
method = sys.argv[1]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    if method == "INVITE":
        my_socket.send(bytes('INVITE sip:'+LINE+' SIP/2.0\r\n', 'utf-8') +
                       b'\r\n')

    if method == "BYE":
        my_socket.send(bytes('BYE sip:'+LINE+' SIP/2.0\r\n', 'utf-8') +
                       b'\r\n')

    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    message_recivied = data.decode('utf-8').split(' ')
    for elementos in message_recivied:
        if method != "BYE" and elementos == '200':
            my_socket.send(bytes('ACK sip:' + LINE.split(':')[0] +
                                 ' SIP/2.0\r\n', 'utf-8') + b'\r\n')
    print("Terminando socket...")

print("Fin.")
