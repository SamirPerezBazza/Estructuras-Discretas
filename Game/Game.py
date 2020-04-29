import pygame
from Generacion import Generacion
import numpy as np
class Game:
    def __init__(self,n,N):
        pygame.init()
        self.cell_width=20
        self.width = n * self.cell_width
        self.screen = pygame.display.set_mode((self.width, self.width))
        self.bg=25,25,25
        self.screen.fill(self.bg)
        self.inicio= Generacion(np.zeros((n,n),dtype=int),N)


    def __iter__(self):
        self.actual=self.inicio
        return self

    def __next__(self):
        if len(self.actual.vivos())>0:
            self.actual=self.actual.siguiente()
            return self.actual
        else:
            raise StopIteration
