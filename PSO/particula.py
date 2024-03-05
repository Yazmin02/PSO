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

        # Imprimir la posición inicial de la partícula
        print("Posición inicial de la partícula:", self.position)
        # Imprimir la velocidad inicial de la partícula
        print("Velocidad inicial de la partícula:", self.velocity)
        # Imprimir la mejor posición inicial de la partícula
        print("Mejor posición inicial de la partícula:", self.best_position)
        # Imprimir el mejor valor inicial de la partícula
        print("Mejor valor inicial de la partícula:", self.best_value)

