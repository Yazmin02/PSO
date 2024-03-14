import copy
import numpy as np
from particula import Particle
from restricciones import ConstraintHandler

class Enjambre:
    def __init__(self, num_particles, num_dimensions, bounds_lower, bounds_upper):
        self.particles = [Particle(num_dimensions, bounds_lower, bounds_upper) for _ in range(num_particles)]
        self.bounds_lower = bounds_lower
        self.bounds_upper = bounds_upper
        self.global_best_position = np.zeros(num_dimensions)
        self.global_best_value = float('inf')  # Inicializa con infinito para minimización

        # Instancia de ConstraintHandler con los límites inferiores y superiores
        self.constraint_handler = ConstraintHandler(bounds_lower, bounds_upper)

    def update_particles(self, inertia, c1, c2, rand1, rand2):
        for particle in self.particles:
            if particle.best_position is None or particle.position is None:
                continue

            new_velocity = (inertia * particle.velocity +
                            c1 * rand1 * (particle.best_position - particle.position) +
                            c2 * rand2 * (self.global_best_position - particle.position))
            new_position = particle.position + new_velocity

        for i in range(len(self.bounds_lower)):
                if new_position[i] > self.bounds_upper[i]:
                    new_position[i] = 2 * self.bounds_upper[i] - new_position[i]
                if new_position[i] < self.bounds_lower[i]:
                    new_position[i] = 2 * self.bounds_lower[i] - new_position[i]

            # Verifica si la nueva posición cumple con las restricciones DEB
        if not self.constraint_handler.check_constraints(new_position):
                new_position = self.constraint_handler.correct_position(new_position)

            # Actualiza la posición y evalúa la función objetivo
        particle.position = new_position
        particle_value = self.evaluate(new_position)

            # Actualiza la mejor posición individual y global
        if particle_value < particle.best_value:
                particle.best_position = copy.deepcopy(new_position)
                particle.best_value = particle_value
        if particle.best_value < self.global_best_value:
                self.global_best_value = particle.best_value
                self.global_best_position = copy.deepcopy(particle.best_position)



    def evaluate(self, position):
        # Coeficientes de la función objetivo
        C1 = 1.715
        C2 = 0.035
        C3 = 4.0565
        C4 = 10.000
        C5 = 3000.0
        C6 = 0.063
        # Desempaqueta las posiciones
        x1, x2, x3, x4, x5, x6, x7 = position
        # Calcula cada término de la función objetivo
        term1 = C1 * x1
        term2 = C2 * x1 * x6
        term3 = C3 * x3
        term4 = C4 * x2
        term5 = C5
        term6 = C6 * x3 * x5        
        # Suma los términos para obtener el valor final de la función objetivo
        result = term1 + term2 + term3 + term4 + term5 - term6    
        print("Valor de evaluación de la partícula:", result)
    
        return result
