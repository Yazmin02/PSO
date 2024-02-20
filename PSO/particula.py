import numpy as np  # Importar la librería NumPy para operaciones numéricas eficientes

class Particle:  # Definir una clase llamada Particle para representar una partícula en PSO
    def __init__(self, num_dimensions, bounds):  # Método especial para inicializar una partícula
        # Inicializar la posición de la partícula aleatoriamente dentro de los límites definidos
        self.position = np.random.uniform(bounds[:, 0], bounds[:, 1], num_dimensions)
        # Inicializar la velocidad de la partícula como un arreglo de ceros
        self.velocity = np.zeros(num_dimensions)
        # Inicializar la mejor posición de la partícula como una copia de su posición actual
        self.best_position = np.copy(self.position)
        # Inicializar el mejor valor (la mejor solución encontrada) de la partícula como infinito
        self.best_value = float('inf')
