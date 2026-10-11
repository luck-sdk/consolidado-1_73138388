import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre                      # str
        self.masa = masa                          # kg (float)
        self.radio = radio                        # metros (float)
        self.distancia_al_sol = distancia_al_sol  # UA (float)
        self.tiene_vida = tiene_vida              # bool

    def calcular_densidad(self):
        """Densidad media en kg/m3 = masa / (4/3 * pi * radio^3)."""
        return self.masa / ((4 / 3) * math.pi * self.radio ** 3)

    def es_planeta_exterior(self):
        """True si la distancia al Sol es mayor a 5.2 UA."""
        return self.distancia_al_sol > 5.2

    def __str__(self):
        tipo = "exterior" if self.es_planeta_exterior() else "interior"
        return (f"Planeta {self.nombre} | densidad: {self.calcular_densidad():.2f} kg/m3 "
                f"| tipo: {tipo}")


tierra = Planeta("Tierra", 5.972e24, 6.371e6, 1.0, True)
jupiter = Planeta("Júpiter", 1.898e27, 6.9911e7, 5.204)
print(tierra)
print(jupiter)
