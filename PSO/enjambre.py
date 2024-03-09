import copy
import numpy as np
from particula import Particle  # Importa la clase Particle desde el módulo particula

class Enjambre:
    def __init__(self, num_particles, num_dimensions, bounds_lower, bounds_upper):
        # Crea instancias de Particle y las almacena en la lista particles
        self.particles = [Particle(num_dimensions, bounds_lower, bounds_upper) for _ in range(num_particles)]
        self.bounds_lower = bounds_lower
        self.bounds_upper = bounds_upper
        self.global_best_position = np.zeros(num_dimensions)
        self.global_best_value = float('inf')  # Inicializa con infinito para minimización

    def update_particles(self, inertia, c1, c2, rand1, rand2):
        for particle in self.particles:
            # Salta la iteración si alguna posición es None
            if particle.best_position is None or particle.position is None:
                continue  
            # Calcula la nueva velocidad y posición de la partícula
            new_velocity = (inertia * particle.velocity +
                            c1 * rand1 * (particle.best_position - particle.position) +
                            c2 * rand2 * (self.global_best_position - particle.position))
            new_position = particle.position + new_velocity

            # Ajusta la nueva posición si se sale de los límites de búsqueda
            for i in range(len(self.bounds_lower)):
                if new_position[i] > self.bounds_upper[i]:
                    new_position[i] = 2*self.bounds_upper[i]-new_position[i]  # Establecer la posición en el límite superior
                if new_position[i] < self.bounds_lower[i]:
                    new_position[i] = 2*self.bounds_lower[i]-new_position[i] # Establecer la posición en el límite inferior

            # Evalúa la nueva posición y actualiza las mejores posiciones individuales y globales
        objective_value = self.evaluate(new_position)
        if self.evaluate(new_position) < particle.best_value:
                particle.best_position = copy.deepcopy(new_position)
                particle.best_value = self.evaluate(new_position)            
        if particle.best_value < self.global_best_value:
                self.global_best_value = particle.best_value
                self.global_best_position = copy.deepcopy(particle.best_position)
                
            # Evalúa la función objetivo para la nueva posición
        objective_value = self.evaluate(new_position)
        print("Valor de la función objetivo:", objective_value)

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
        return result

    def apply_DEB_constraints(self, particles):
        #Aplica las restricciones DEB (Dominance-based Sorting) a una partícula objetivo.
        best_particle = None
        best_SVR = float('inf')
        # Itera sobre todas las partículas para encontrar la mejor según las reglas de Deb
        for current_particle in self.particles:
            SVR = self.calculate_SVR(current_particle)
            feasibility = "Factible" if SVR == 0 else "Infactible"
            # Si la partícula actual es factible y tiene un mejor valor de la función objetivo, 
            # o si es factible y la mejor partícula es infactible, actualiza la mejor partícula
            if SVR == 0 and (best_particle is None or current_particle.best_value < best_particle.best_value or best_SVR > 0):
                best_particle = current_particle
                best_SVR = SVR
        # Si no se encontró ninguna partícula factible, selecciona la que tenga la menor violación
        if best_particle is None:
            for current_particle in self.particles:
                SVR = self.calculate_SVR(current_particle)
                if SVR < best_SVR:
                    best_particle = current_particle
                    best_SVR = SVR
        best_feasibility = "Factible" if best_SVR == 0 else "Infactible"
        return best_particle

    def calculate_SVR(self, particle):

        SVR = 0
        # Coeficientes para las restricciones del tipo: Cx <= d (desigualdad)
        C7 = 0.59553571E-2
        C8 = 0.88392857
        C9 = 0.11756250
        C10 = 1.10880000
        C11 = 0.13035330
        C12 = 0.00660330 
        C13 = 0.66173269E-3
        C14 = 0.17239878E-1
        C15 = 0.56595559E-2
        C16 = 0.19120592E-1
        C17 = 0.19120592E+2
        C18 = 1.08702000
        C19 = 0.32175000
        C20 = 0.03762000
        C21 = 0.00619800 
        C22 = 0.24623121E+4
        C23 = 0.25125634E+2
        C24 = 0.16118996E+3
        C25 = 5000.0 
        C26 = 0.48951000E+6
        C27 = 0.44333333E+2
        C28 = 0.33000000
        C29 = 0.02255600
        C30 = 0.00759500
        C31 = 0.00061000
        C32 = 0.0005
        C33 = 0.81967200 
        C34 = 0.81967200
        C35 = 24500.0
        C36 = 250.0
        C37 = 0.10204082E-1
        C38 = 0.12244898E-4
        C39 = 0.00006250
        C40 = 0.00006250
        C41 = 0.00007625
        C42 = 1.22
        C43 = 1.0
        C44 = 1.0

        # Restricciones del tipo: Cx <= d (desigualdad)
        for i in range(len(particle.position)):  # Usar un rango basado en la longitud de la posición de la partícula
            SVR += max(0, C7 * particle.position[5]**2 + C8 * (particle.position[0]**-1) * particle.position[2] - C9 * particle.position[5] - 1)
            SVR += max(0, C10 * particle.position[0] * (particle.position[2]**-1) + C11 * particle.position[0] * (particle.position[2]**-1) * particle.position[5] - C12 * particle.position[0] * (particle.position[2]**-1) * particle.position[5]**2 - 1)
            SVR += max(0, C13 * particle.position[5]**2 + C14 * particle.position[4] - C15 * particle.position[3] - C16 * particle.position[5] - 1)
            SVR += max(0, C17 * (particle.position[4]**-1) + C18 * (particle.position[4]**-1) * particle.position[5] + C19 * particle.position[3] * (particle.position[4]**-1) - C20 * (particle.position[4]**-1) * particle.position[5]**2 - 1)
            SVR += max(0, C21**particle.position[6] + C22 * particle.position[1] * (particle.position[2]**-1) * (particle.position[3]**-1) - C23 * particle.position[1] * (particle.position[2]**-1) - 1)
            SVR += max(0, C24 * (particle.position[6]**-1) + C25 * particle.position[1] * (particle.position[2]**-1) * (particle.position[6]**-1) - C26 * particle.position[1] * (particle.position[2]**-1) * (particle.position[3]**-1) * (particle.position[6]**-1) - 1)
            SVR += max(0, C27 * (particle.position[4]**-1) + C28 * (particle.position[4]**-1) * particle.position[6] - 1)
            SVR += max(0, C29 * particle.position[4] - C30 * particle.position[6] - 1)
            SVR += max(0, C31 * particle.position[2] - C32 * particle.position[0] - 1)
            SVR += max(0, C33 * particle.position[0] * (particle.position[2]**-1) + C34 * (particle.position[2]**-1) - 1)
            SVR += max(0, C35 * particle.position[1] * (particle.position[2]**-1) * (particle.position[3]**-1) - C36 * particle.position[1] * (particle.position[2]**-1) - 1)
            SVR += max(0, C37 * particle.position[3] + C38 * (particle.position[1]**-1) - 1)
            SVR += max(0, C39 * particle.position[0] * particle.position[5] + C40 * particle.position[0] - C41 * particle.position[2] - 1)
            SVR += max(0, C42 * (particle.position[0]**-1) * particle.position[2] + C43 * (particle.position[0]**-1) - C44 * particle.position[5] - 1)

        return SVR

