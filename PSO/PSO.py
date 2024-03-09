import copy
import numpy as np
from enjambre import Enjambre

class PSO:
    def __init__(self, num_particles, num_dimensions, bounds_lower, bounds_upper, max_iterations, inertia, c1, c2):
        self.swarm = Enjambre(num_particles, num_dimensions, bounds_lower, bounds_upper)
        self.max_iterations = max_iterations
        self.inertia = inertia
        self.c1 = c1
        self.c2 = c2
        self.global_best_position = None
        self.global_best_value = float('inf')

    def update_global_best(self):
        """
        Actualiza la mejor posición global del enjambre.
        Recorre todas las partículas del enjambre y actualiza la mejor posición global
        si se encuentra una partícula con un valor objetivo mejor que el mejor valor global actual.
        """
        for particle in self.swarm.particles:
            # Comprueba si la mejor posición de la partícula actual es mejor que la mejor global actual
            if particle.best_value < self.global_best_value:
                # Actualiza la mejor posición global y su valor asociado
                self.global_best_value = particle.best_value
                self.global_best_position = copy.deepcopy(particle.best_position)

    def optimize(self):
        """
        Optimiza el enjambre de partículas durante un número especificado de iteraciones.
        Realiza la optimización del enjambre durante un número máximo de iteraciones.
        Actualiza la mejor posición global y actualiza las partículas del enjambre en cada iteración.
        Al final, aplica las restricciones DEB a cada partícula y devuelve la mejor posición global
        encontrada y su valor asociado.
        """
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
            self.swarm.apply_DEB_constraints(particle)
        # Devuelve la mejor posición global y su valor asociado
        return self.global_best_position, self.global_best_value
