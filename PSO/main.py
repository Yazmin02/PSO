import numpy as np
from PSO import PSO
# Define el número de partículas en el enjambre
num_particles = 50
# Define el número de dimensiones del espacio de búsqueda
num_dimensions = 7
# Define los límites inferiores para cada dimensión
bounds_lower = np.array([1500, 1, 3000, 85, 90, 3, 145])
# Define los límites superiores para cada dimensión
bounds_upper = np.array([2000, 120, 3500, 93, 95, 12, 162])
# Define el número máximo de iteraciones que el algoritmo realizará
max_iterations = 100
# Define el coeficiente de inercia que controla la influencia de la velocidad anterior en la nueva velocidad
inertia = 0.8
# Define el coeficiente cognitivo que controla la influencia de la mejor posición de la partícula en la nueva velocidad
c1 = 1.8
# Define el coeficiente social que controla la influencia de la mejor posición global en la nueva velocidad
c2 = 3.9
pso = PSO(num_particles, num_dimensions, bounds_lower, bounds_upper, max_iterations, inertia, c1, c2)
best_solution, best_value = pso.optimize()

# Imprime la mejor solución encontrada y su valor asociado
print("Mejor solución:", best_solution)
