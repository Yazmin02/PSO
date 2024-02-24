import numpy as np
from FO import PSO

# Ejemplo de uso:
num_particles = 50
num_dimensions = 7
bounds = np.array([[1500, 2000],
                   [1, 120],
                   [3000, 3500],
                   [85, 93],
                   [90, 95],
                   [3, 12],
                   [145, 162]])
max_iterations = 100
inertia = 0.5
c1 = 1.5
c2 = 1.5
pso = PSO(num_particles, num_dimensions, bounds, max_iterations, inertia, c1, c2)
best_solution, best_value = pso.optimize()
print("Mejor solución:", best_solution)
print("Mejor valor:", best_value)
