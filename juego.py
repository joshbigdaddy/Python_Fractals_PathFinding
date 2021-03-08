import pygame, sys, random
from pygame.locals import *
from mapa import Mapa, distancia, VACIO, MURO
import color_mapa

LADO_CELDA  = 10
ANCHO_MAPA  = 100
ALTO_MAPA = 100


pygame.init()

from enum import Enum

class Estado(Enum):
    PATRULLAR = 1
    BUSCAR = 2
    RASTREAR = 3
    LUCHA = 4
    HUIR = 5
    MUERTO = 6


class Monstruo():
    def __init__(self, posicion):
        self.posicion = posicion
        self.estado = Estado.PATRULLAR
        self.lentitud = 5
        self.vida = 10
        self.armadura = 2
        self.turno = 0

        self.switcher = {
            Estado.PATRULLAR: self.patrullar,
            Estado.BUSCAR: self.buscar,
            Estado.RASTREAR: self.rastrear,
            Estado.HUIR: self.huir,
            Estado.LUCHA: self.luchar
        }
        self.distancia_visto = None
        self.distancia_olido = None
        self.max_dist_olfato = 10
        self.max_dist_vista = 20


    def oler(self):
        pass

    def ver(self):
        pass

    def percibir(self):
        pass

    def buscar(self):
        pass

    def rastrear(self):
        pass

    def huir(self):
        pass

    def patrullar(self):
        pass

    def atacar(self):
        return (random.randint(0, 7))

    def defender(self, ataque):
        pass

    def luchar(self):
        pass

    def actualizar(self):
        pass



class Jugador():
    def __init__(self, posicion):
        self.posicion = posicion
        self.movimientos = []
        self.vida = 10
        self.armadura = 5

    def atacar(self):
        return(random.randint(0, 10))

    def defender(self, ataque):
        if(ataque > self.armadura):
            self.vida -= (ataque-self.armadura)


    def actualizar(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            print(event)
            if event.type == KEYDOWN:
                newPos = list(self.posicion)
                if event.key == K_RIGHT :
                    newPos[1] += 1
                if event.key == K_LEFT :
                    newPos[1] -= 1
                if event.key == K_UP :
                    newPos[0] -= 1
                if event.key == K_DOWN :
                    newPos[0] += 1
                newPos = tuple(newPos)

                if mapa.esta_dentro(newPos) and (mapa[newPos] == VACIO):
                    print(newPos)
                    print(mapa[tuple(newPos)])
                    posiciones = []
                    self.posicion = newPos
                print(self.posicion)
                if event.key == K_SPACE:
                    for monstruo in monstruos:
                        if(distancia(monstruo.posicion,self.posicion)<=2):
                            monstruo.defender(self.atacar())

            elif event.type == MOUSEBUTTONDOWN:
                print((event.pos[0] // LADO_CELDA, event.pos[1] // LADO_CELDA))
                self.movimientos = mapa.buscar_camino( self.posicion, (event.pos[1] // LADO_CELDA, event.pos[0] // LADO_CELDA))
                print(self.movimientos)

        if (len(self.movimientos) > 0):
            self.posicion = self.movimientos.pop(0)


mapa = Mapa(ANCHO_MAPA,ALTO_MAPA,LADO_CELDA)
#mapa.generar_aleatorio()
#mapa.generar_automata()


jugador = Jugador((0,0))
monstruos = [Monstruo((0,ANCHO_MAPA-1)), Monstruo((ALTO_MAPA-1,ANCHO_MAPA-1)), Monstruo((ALTO_MAPA-1,0))]

while True:

    jugador.actualizar(pygame.event.get())

    mapa.mostrar_mapa()

    mapa.mostrar_celda(jugador.posicion, color_mapa.ROJO)

    for monstruo in monstruos:
        monstruo.actualizar()
        color = color_mapa.AZUL
        if(monstruo.estado == Estado.MUERTO):
            color = color_mapa.VERDE
        mapa.mostrar_celda(monstruo.posicion,color)

    pygame.display.update()
    pygame.time.wait(100)
