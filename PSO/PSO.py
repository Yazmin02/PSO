import copy
import numpy as np  
from enjambre import Enjambre  

class PSO:
    def __init__(self, num_particles, num_dimensions, bounds, max_iterations, inertia, c1, c2):
        # Inicialización de la instancia de PSO con parámetros dados
        self.swarm = Enjambre(num_particles, num_dimensions, bounds)  # Inicializa el enjambre
        self.max_iterations = max_iterations  # Número máximo de iteraciones
        self.inertia = inertia  # Factor de inercia
        self.c1 = c1  # Factor cognitivo
        self.c2 = c2  # Factor social
        self.global_best_position = None  # Inicializa la mejor posición global como None
        self.global_best_value = float('inf')  # Inicializa el mejor valor global como infinito positivo

    def update_global_best(self):
        # Actualiza la mejor posición global
        for particle in self.swarm.particles:
            if particle.best_value < self.global_best_value:
                self.global_best_value = particle.best_value
                self.global_best_position = copy.deepcopy(particle.best_position)

    def optimize(self):
        for _ in range(self.max_iterations):
            self.update_global_best()
            rand1 = np.random.rand()
            rand2 = np.random.rand()
            self.swarm.update_particles(self.inertia, self.c1, self.c2, rand1, rand2)

        for particle in self.swarm.particles:
            self.swarm.apply_DEB_constraints(particle)
        return self.global_best_position, self.global_best_value

