import numpy as np
from enjambre import enjambre

class PSO:
    def __init__(self, num_particles, num_dimensions, bounds, max_iterations, inertia, c1, c2):
        self.swarm = Swarm(num_particles, num_dimensions, bounds)
        self.max_iterations = max_iterations
        self.inertia = inertia
        self.c1 = c1
        self.c2 = c2
        self.global_best_position = None
        self.global_best_value = float('inf')

    def update_global_best(self):
        for particle in self.swarm.particles:
            if particle.best_value < self.global_best_value:
                self.global_best_value = particle.best_value
                self.global_best_position = np.copy(particle.best_position)

    def optimize(self):
        for _ in range(self.max_iterations):
            self.update_global_best()
            rand1 = np.random.rand()
            rand2 = np.random.rand()
            self.swarm.update_particles(self.inertia, self.c1, self.c2, rand1, rand2)
        return self.global_best_position, self.global_best_value
