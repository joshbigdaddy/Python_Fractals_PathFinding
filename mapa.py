import pygame
import random
import color_mapa
import math

VACIO  = 0
MURO = 1
ROJO = 2
colores_mapa =   {
                VACIO: color_mapa.NEGRO,
                MURO: color_mapa.MARRON,
                ROJO: color_mapa.ROJO,
            }

#JUGADOR = pygame.image.load('jugador.png')

def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
class Celda:
    def __init__(self,camino,coste_acum,actual,cerrados):
        self.camino=camino
        self.coste_acum = coste_acum
        self.actual = actual
        self.cerrados=cerrados
class Mapa:
    def __init__(self, ancho_mapa, alto_mapa, lado_celda):
        self.ancho_mapa = ancho_mapa
        self.alto_mapa = alto_mapa
        self.lado_celda = lado_celda
        self.mapa = {(x, y) : VACIO for x in range(self.ancho_mapa) for y in range(self.alto_mapa)}
        self.pantalla = pygame.display.set_mode((self.ancho_mapa * self.lado_celda, self.alto_mapa * self.lado_celda))

    def generar_aleatorio(self):
        for x in range(self.ancho_mapa):
            for y in range(self.alto_mapa):
                seed=random.randint(0, 1)
                valor_mapa = MURO if seed == 1 else VACIO
                self.mapa[x,y]= valor_mapa       

    def generar_automata(self):
        mapa_2= self.mapa.copy()
        for celda in self.mapa:
            vecinos_total = self.vecinos(celda)
            vecinos_abiertos=self.abiertos(celda)
            if len(vecinos_abiertos) / len(vecinos_total) >= 0.5:
                mapa_2[celda]=VACIO
            else:
                mapa_2[celda]=MURO
        self.mapa=mapa_2
        pass

    def __getitem__(self,celda):
        return self.mapa[celda]

    def esta_dentro(self, celda):
        (x, y) = celda
        return (x >= 0) and (x < self.ancho_mapa) and (y >= 0) and (y < self.alto_mapa)

    def vecinos(self, celda):
        (x,y) = celda
        celda_1 = (x,y-1)
        celda_2 = (x,y+1)
        celda_3 = (x+1,y-1)
        celda_4 = (x+1,y)
        celda_5 = (x-1,y+1)
        celda_6 = (x-1,y)
        celda_7 = (x+1,y+1)
        celda_8 = (x-1,y-1)
        vecinos = []
        vecinos_final=[]
        vecinos.append(celda_1)
        vecinos.append(celda_2)
        vecinos.append(celda_3)
        vecinos.append(celda_4)
        vecinos.append(celda_5)
        vecinos.append(celda_6)
        vecinos.append(celda_7)
        vecinos.append(celda_8)
        for vecino in vecinos:
            if self.esta_dentro(vecino):
                vecinos_final.append(vecino)
        return vecinos_final

    def abiertos(self, celda):
        abiertos = []
        ##los vecinos que no son muros
        vecinos = self.vecinos(celda)
        for vecino in vecinos:
            if mapa[vecino] == VACIO:
                abiertos.append(vecino)
        return abiertos

    def buscar_camino_recto(self, origen, destino):
        camino = []
        
        return camino


    def depth(self,origen,destino,path):
        abiertos=self.abiertos(origen)
        for celda in abiertos:
            if celda not in path:
                path.append(celda)
                self.depth(celda,destino,path)
        return path
    def buscar_camino(self, origen, destino):
        path=[]
        for celda in self.abiertos(origen):
            path.append(celda)
            if celda == destino:
                break
            else:
                self.depth(celda,destino,path)
        return path
    
    def mostrar_mapa(self):
        for y in range(self.alto_mapa):
            for x in range(self.ancho_mapa):
                 #PANTALLA.blit(textures[mapa[row][column]], (column*self.lado_celda,row*self.lado_celda))
                self.mostrar_celda((x,y), colores_mapa[self.mapa[(x,y)]])

    def mostrar_celda(self, celda, color):
        (x,y) = celda
        pygame.draw.rect(self.pantalla, color,
                         (y * self.lado_celda, x * self.lado_celda, self.lado_celda, self.lado_celda))

    
    def A_star(self,origen,destino,path):
        coste_acum = len(path)
        closed = []
        if origen==destino:
            return path
        else :
            closed = [origen]
            path = [origen]
            opened = self.abiertos(origen)
            min_f = math.inf
            min_pos = origen
            for op in opened:
                if op not in closed:
                    a=distancia(op,destino)
                    if(a<min_f):
                        min_f=a
                        mid_pos=op
            closed.append(min_pos)
            
            
            

if __name__ == '__main__':

    mapa = Mapa(20,20,10)
    mapa.mapa[(10, 10)]=MURO
    mapa.mapa[(11, 11)] = MURO
    
    mapa.generar_aleatorio()
    #cuanto mas iteramos mas se van marcando los caminos
    for i in range(1):
        mapa.generar_automata()

    pasos = mapa.buscar_camino((1,0),(12,19))

    for paso in pasos:
        print(paso)
        mapa.mostrar_mapa()
        mapa.mostrar_celda(paso, color_mapa.ROJO)
        pygame.display.update()
        pygame.time.wait(1000)
        
    mapa.mostrar_mapa()
    pygame.display.update()
    pygame.time.wait(1000)

