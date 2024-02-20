import numpy as np
from FO import PSO

# Definir constantes para la función objetivo y restricciones
C1 = 1
C2 = 2
C3 = 3
C4 = 4
C5 = 5
C6 = 6
C7 = 7
C8 = 8
C9 = 9
C10 = 10
C11 = 11
C12 = 12
C13 = 13
C14 = 14
C15 = 15
C16 = 16
C17 = 17
C18 = 18
C19 = 19
C20 = 20
C21 = 21
C22 = 22
C23 = 23
C24 = 24
C25 = 25
C26 = 26
C27 = 27
C28 = 28
C29 = 29
C30 = 30
C31 = 31
C32 = 32
C33 = 33
C34 = 34
C35 = 35
C36 = 36
C37 = 37
C38 = 38
C39 = 39
C40 = 40
C41 = 41
C42 = 42
C43 = 43

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
