import numpy as np
import pygame
class Generacion:
    def __init__(self, anterior, elementos):
        self.pausa=False
        self.salir=False
        self.anterior=anterior
        self.elementos=elementos
        self.tam=len(self.anterior)
        self.newGeneracion=np.copy(self.anterior)
        for tupla in self.elementos:
            self.newGeneracion[tupla[0],tupla[1]]=1


    def vivos(self):
        return self.elementos

    def nacimientos(self):
        nuevos_nacimientos=[]

        for x in range(self.tam):
            for y in range(self.tam):

                vecino= self.newGeneracion[(x-1)%self.tam,(y-1)%self.tam]+\
                        self.newGeneracion[(x)%self.tam,(y-1)%self.tam]+\
                        self.newGeneracion[(x+1)%self.tam,(y-1)%self.tam]+\
                        self.newGeneracion[(x-1)%self.tam,(y)%self.tam]+\
                        self.newGeneracion[(x+1)%self.tam,(y)%self.tam]+\
                        self.newGeneracion[(x-1)%self.tam,(y+1)%self.tam]+\
                        self.newGeneracion[(x)%self.tam,(y+1)%self.tam]+\
                         self.newGeneracion[(x+1)%self.tam,(y+1)%self.tam]
                if self.newGeneracion[x,y]==0 and vecino==3:
                    nuevos_nacimientos.append((x,y))
        return nuevos_nacimientos

    def muertes(self):
        nuevos_muertos=[]
        for x in range(self.tam):
            for y in range(self.tam):
                vecino=self.newGeneracion[(x-1)%self.tam,(y-1)%self.tam]+\
                    self.newGeneracion[(x)%self.tam,(y-1)%self.tam]+\
                    self.newGeneracion[(x+1)%self.tam,(y-1)%self.tam]+\
                    self.newGeneracion[(x-1)%self.tam,(y)%self.tam]+\
                    self.newGeneracion[(x+1)%self.tam,(y)%self.tam]+\
                    self.newGeneracion[(x-1)%self.tam,(y+1)%self.tam]+\
                    self.newGeneracion[(x)%self.tam,(y+1)%self.tam]+\
                    self.newGeneracion[(x+1)%self.tam,(y+1)%self.tam]
                if self.newGeneracion[x,y]==1 and (vecino<2 or vecino>3):
                    nuevos_muertos.append((x,y))
        return nuevos_muertos

    def siguiente(self):
        ev=pygame.event.get()
        for event in ev:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    self.pausa=not self.pausa
                if event.key==pygame.K_ESCAPE:
                    self.salir=True
        if not self.pausa:
            if not self.salir:
                vivos=self.nacimientos()
                muertos=self.muertes()
            else:
                vivos=[]
                muertos=self.nacimientos()
            self.elementos=vivos
            for x in range(self.tam):
                for y in range(self.tam):
                    if (x,y) in vivos:
                        self.newGeneracion[x, y] = 1
                    elif(x,y) in muertos:
                        self.newGeneracion[x, y] = 0
        return self
