import copy
import numpy as np

class Particle:
    def __init__(self, num_dimensions, bounds_lower, bounds_upper):
        # Inicializa la posición de la partícula aleatoriamente dentro de los límites definidos
        self.position = np.random.uniform(bounds_lower, bounds_upper, num_dimensions)
        
        # Inicializa la velocidad de la partícula como un arreglo de ceros
        self.velocity = np.zeros(num_dimensions)
        
        # Inicializa la mejor posición de la partícula como una copia de su posición actual
        self.best_position = copy.deepcopy(self.position)
        
        # Inicializa el mejor valor (la mejor solución encontrada) de la partícula como infinito
        self.best_value = float('inf')
