import numpy as np
from particula import Particle

class Swarm:
    def __init__(self, num_particles, num_dimensions, bounds):
        self.particles = [Particle(num_dimensions, bounds) for _ in range(num_particles)]
        self.bounds = bounds
        self.global_best_position = np.zeros(num_dimensions)
        self.global_best_value = float('inf')

    def update_particles(self, inertia, c1, c2, rand1, rand2):
        for particle in self.particles:
            if particle.best_position is not None and particle.position is not None:  # Verificar que las posiciones sean válidas
                # Actualizar velocidad
                new_velocity = (inertia * particle.velocity +
                                c1 * rand1 * (particle.best_position - particle.position) +
                                c2 * rand2 * (self.global_best_position - particle.position))
                
                # Actualizar posición
                new_position = particle.position + new_velocity
                new_position = np.clip(new_position, self.bounds[:, 0], self.bounds[:, 1])  # Ajustar dentro de los límites
                particle.position = new_position

                # Aplicar reglas DEB para las restricciones
                self.apply_DEB_constraints(particle)

                # Actualizar mejor posición local
                if self.evaluate(new_position) < particle.best_value:
                    particle.best_position = np.copy(new_position)
                    particle.best_value = self.evaluate(new_position)

                # Actualizar mejor posición global
                if particle.best_value < self.global_best_value:
                    self.global_best_value = particle.best_value
                    self.global_best_position = np.copy(particle.best_position)

    def evaluate(self, position):
        # Función objetivo a minimizar
        x1, x2, x3, x4, x5, x6, x7 = position
        return x1 + x1*x6 + x3 + x2 + x3*x5

