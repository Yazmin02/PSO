import numpy as np
from particula import Particle  

class Enjambre:
    def __init__(self, num_particles, num_dimensions, bounds):
        self.particles = [Particle(num_dimensions, bounds) for _ in range(num_particles)]
        self.bounds = bounds
        self.global_best_position = np.zeros(num_dimensions)
        self.global_best_value = float('inf')  # Inicializar con infinito para minimización
      
      # Imprimir la primera partícula generada
        print("Primera partícula generada:")
        print("Posición:", self.particles[0].position)
        print("Velocidad:", self.particles[0].velocity)


    def update_particles(self, inertia, c1, c2, rand1, rand2):
        for particle in self.particles:
            if particle.best_position is not None and particle.position is not None: 
                new_velocity = (inertia * particle.velocity +
                                c1 * rand1 * (particle.best_position - particle.position) +
                                c2 * rand2 * (self.global_best_position - particle.position))

                new_position = particle.position + new_velocity

                #print("Velocidad de la partícula:", new_velocity)
                #print("Nueva posición de la partícula:", new_position)
                for i in range(len(self.bounds)):
                    if new_position[i] < self.bounds[i, 0]:
                        new_position[i] = 2 * self.bounds[i, 0] - new_position[i]
                        while new_position[i] < self.bounds[i, 0]:
                            new_position[i] += np.abs(self.bounds[i, 1] - self.bounds[i, 0])
                    if new_position[i] > self.bounds[i, 1]:
                        new_position[i] = 2 * self.bounds[i, 1] - new_position[i]
                        while new_position[i] > self.bounds[i, 1]:
                            new_position[i] += np.abs(self.bounds[i, 1] - self.bounds[i, 0])
                
                #print("Posición ajustada de la partícula:", new_position)

                if self.evaluate(new_position) < particle.best_value:
                    particle.best_position = np.copy(new_position)
                    particle.best_value = self.evaluate(new_position)

                if particle.best_value < self.global_best_value:
                    self.global_best_value = particle.best_value
                    self.global_best_position = np.copy(particle.best_position)

                #print("Mejor posición global:", self.global_best_position)
                #print("Mejor valor global:", self.global_best_value)
                     # Evaluar la función objetivo para la nueva posición
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
        
        # Desempaquetar las posiciones
        x1, x2, x3, x4, x5, x6, x7 = position
        
        # Calcular cada término de la función objetivo
        term1 = C1 * x1
        term2 = C2 * x1 * x6
        term3 = C3 * x3
        term4 = C4 * x2
        term5 = C5
        term6 = C6 * x3 * x5
        
        # Imprimir cada término individualmente
        print("Término 1:", term1)
        print("Término 2:", term2)
        print("Término 3:", term3)
        print("Término 4:", term4)
        print("Término 5:", term5)
        print("Término 6:", term6)
        
        # Sumar los términos para obtener el valor final de la función objetivo
        result = term1 + term2 + term3 + term4 + term5 - term6
        print("Resultado final de la evaluación:", result)
        
        # Retornar el valor final de la función objetivo
        return result

 
    def apply_DEB_constraints(self, particle):
        best_particle = None
        best_SVR = float('inf')

        # Iterar sobre todas las partículas para encontrar la mejor según las reglas de Deb
        for current_particle in self.particles:
            SVR = self.calculate_SVR(current_particle)
            feasibility = "Factible" if SVR == 0 else "Infactible"
            print(f"Violaciones de la partícula ({feasibility}): {SVR}")

            # Si la partícula actual es factible y tiene un mejor valor de la función objetivo, o si es factible y la mejor partícula es infactible, actualiza la mejor partícula
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

        # Imprimir la mejor partícula seleccionada y su estado de factibilidad+-
        best_feasibility = "Factible" if best_SVR == 0 else "Infactible"
        print(f"Mejor partícula seleccionada ({best_feasibility}): {best_SVR}")

        return best_particle


    def calculate_SVR(self, particle):
        SVR = 0
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
