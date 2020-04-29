from Game import Game
import random as r
import pygame
import time
from tkinter import *
from tkinter import messagebox
# n=int(input("Ingrese el tamaño de la casilla: \n"))
n=10
cont=0
maxElementos=int(input("Ingrese el número de elementos generados al azar: \n"))
iniciales=[]
while(cont<maxElementos):
    x= r.randint(0,n-1)
    y= r.randint(0,n-1)
    if  (x,y) not in iniciales:
        iniciales.append((x,y))
        cont+=1
# print(len(iniciales))
# print(iniciales)
game = Game(n,iniciales)
Tk().wm_withdraw()
messagebox.showinfo("Información importante","Para pausar presione la tecla P.\n"
                    "Para salir presione la tecla Esc")

for generacion in game:
    pygame.event.pump()
    game.screen.fill(game.bg)
    time.sleep(0.1)

    for x in range(n):
        for y in range(n):
            poly=[((x)*20,y*20),
                ((x+1)*20,y*20),
                ((x+1)*20,(y+1)*20),
                ((x)*20,(y+1)*20)]
            if generacion.newGeneracion[x,y]==0:
                pygame.draw.polygon(game.screen,(128,128,128),poly, 1)
            else:
                pygame.draw.polygon(game.screen,(255,255,255),poly, 0)
    pygame.display.flip()

