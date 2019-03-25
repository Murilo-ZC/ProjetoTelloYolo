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
import cv2
import numpy as np
import time

# Speed of the drone
S = 60
# Frames per second of the pygame window display
#FPS = 30

#Create a Tello
tello = Tello()

#Connect to Tello
tello.connect()

#Starts Tello VideoStream
tello.streamon()

#Takeoff the drone
tello.takeoff()
#Mantem o programa rodando
while True:
    can = tello.get_video_capture()
    #Get a Tello Frame
    resultado, frame = can.read()
    #Show the drone image
    cv2.imshow("Titulo da img", frame)
    #Sleep FPS time
#    time.sleep(1 / FPS)
    #Close the application
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
#Land the drone
tello.land()
#Close Tello Stream
tello.end()
#Fecha qualquer tela que estiver aberta
cv2.destroyAllWindows()