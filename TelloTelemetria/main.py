# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:02:32 2019

@author: Murilo
"""
#Git utilizado
#https://github.com/damiafuentes/DJITelloPy
#import os
#
#os.system("python -m pip install djitellopy")

from djitellopy import Tello
import numpy as np
import time


#Method to getDroneData(Tello)
def getDroneData(tello):
    dados = {}
    #Pega os dados de velocidade - cm/s
    dados["speed"] = str(tello.get_speed())
    dados["battery"] = str(tello.get_battery())
    dados["height"] = str(tello.get_height()) #cm
    dados["imu"] = str(tello.get_attitude())
    dados['barometer'] = str(tello.get_barometer())
    return dados


# Speed of the drone
S = 60
# Frames per second of the pygame window display
FPS = 10

#Create a Tello
tello = Tello()

#Connect to Tello
tello.connect()



#Mantem o programa rodando
#while True:
amostras = []
for i in range(100):
    #get data from drone
    amostras.append(getDroneData(tello))
    #Sleep FPS time
    time.sleep(1 / FPS)
   
#Show getted data
for amostra in amostras:
    print(amostra)

#Close Tello Stream
tello.end()
#Fecha qualquer tela que estiver aberta
cv2.destroyAllWindows()