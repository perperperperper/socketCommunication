#!/usr/bin/env python3
# TCP server. Will listen and receive data until client sends 'q'
# Adapted/Elaborated by Per dahlstrøm
import socket, time      # Fetch the socket module

HOST = '127.0.0.1'  # Put the IP addrress of the server here
PORT = 65432        # Port to listen on should be > 1023

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    addresAndPort = s.getsockname() # Get tuple with IP and Port addresses
    print('Awaiting connection on IP: ',addresAndPort[0],\
                              ' Port: ',addresAndPort[1])
    connection, fromAddress = s.accept() # On connection, create socket
    print('Connection from:', fromAddress)
    return connection

def getSensorData():
    connectionSocket = connect()
    receivedData = (connectionSocket.recv(16)).decode('utf-8')
    connectionSocket.close()
    print('Connection closed')
    return receivedData

def storeSensorData(d):
    # Put code to store data here
    print('Stored sensor data: ',d)

while True:
    mySensordata = getSensorData()
    storeSensorData(mySensordata)   # Do things based on the sensor data
    time.sleep(0.5)                 # Sleep time syncronized with sender

print('Connection stopped.')