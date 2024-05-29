import numpy as np
from enjambre import Enjambre
from restricciones import ConstraintHandler

class PSO:
    def __init__(self, num_particles, num_dimensions, bounds_lower, bounds_upper, max_iterations, inertia, c1, c2):
        # Inicializa un enjambre con las partículas y sus dimensiones, límites inferiores y superiores
        self.swarm = Enjambre(num_particles, num_dimensions, bounds_lower, bounds_upper)
        self.max_iterations = max_iterations
        self.inertia = inertia
        self.c1 = c1
        self.c2 = c2
        self.global_best_position = None
        self.global_best_value = float('inf')
        self.constraint_handler = ConstraintHandler(bounds_lower, bounds_upper)

    def update_global_best(self):        
        # Recorre cada partícula en el enjambre
        for particle in self.swarm.particles:
            # Si el valor objetivo de la partícula es mejor que el mejor valor global actual
            if particle.best_value < self.global_best_value:
                # Actualiza el mejor valor global y la mejor posición global
                self.global_best_value = particle.best_value
                self.global_best_position = np.copy(particle.best_position)

    def optimize(self):
        # Recorre cada iteración hasta el máximo número de iteraciones
        for _ in range(self.max_iterations):
            # Actualiza la mejor posición global en cada iteración
            self.update_global_best()
            # Genera valores aleatorios para cálculos posteriores
            rand1 = np.random.rand()
            rand2 = np.random.rand()
            # Actualiza las partículas del enjambre
            self.swarm.update_particles(self.inertia, self.c1, self.c2, rand1, rand2)
            # Aplica las restricciones DEB a cada partícula del enjambre
            for particle in self.swarm.particles:
                # Verifica si la posición de la partícula cumple con las restricciones
                if not self.constraint_handler.check_constraints(particle.position):
                    # Corrige la posición de la partícula si no cumple con las restricciones
                    particle.position = self.constraint_handler.correct_position(particle.position)
                    # Actualiza la mejor posición de la partícula
                    particle.best_position = np.copy(particle.position)
                    # Evalúa la nueva posición de la partícula
                    particle.best_value = self.swarm.evaluate(particle.position)
                    # Si el nuevo valor es mejor que el mejor valor global, lo actualiza
                    if particle.best_value < self.global_best_value:
                        self.global_best_value = particle.best_value
                        self.global_best_position = np.copy(particle.best_position)
        # Imprime el mejor valor de la función objetivo encontrado después de todas las iteraciones
        print("Mejor valor de la función objetivo encontrado:", self.global_best_value)
        # Devuelve la mejor posición global y su valor asociado
        return self.global_best_position, self.global_best_value
