import numpy as np
from PSO import PSO

# Ejemplo de uso:
num_particles = 50
num_dimensions = 7
bounds_lower = np.array([1500, 1, 3000, 85, 90, 3, 145])
bounds_upper = np.array([2000, 120, 3500, 93, 95, 12, 162])
max_iterations = 100
inertia = 0.8
c1 = 1.8
c2 = 3.9
pso = PSO(num_particles, num_dimensions, bounds_lower, bounds_upper, max_iterations, inertia, c1, c2)
best_solution, best_value = pso.optimize()
print("Mejor solución:", best_solution)
