import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre                      # str
        self.masa = masa                          # kg (float)
        self.radio = radio                        # metros (float)
        self.distancia_al_sol = distancia_al_sol  # UA (float)
        self.tiene_vida = tiene_vida              # bool
