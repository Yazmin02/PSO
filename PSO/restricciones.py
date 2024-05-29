import numpy as np

class ConstraintHandler:
    def __init__(self, bounds_lower, bounds_upper):
        # Almacena los límites inferiores y superiores
        self.bounds_lower = bounds_lower
        self.bounds_upper = bounds_upper

        # Define los coeficientes de las restricciones DEB
        self.coefficients = {
            7: 0.59553571E-2, 8: 0.88392857, 9: 0.11756250, 10: 1.10880000,
            11: 0.13035330, 12: 0.00660330, 13: 0.66173269E-3, 14: 0.17239878E-1,
            15: 0.56595559E-2, 16: 0.19120592E-1, 17: 0.19120592E+2, 18: 1.08702000,
            19: 0.32175000, 20: 0.03762000, 21: 0.00619800, 22: 0.24623121E+4,
            23: 0.25125634E+2, 24: 0.16118996E+3, 25: 5000.0, 26: 0.48951000E+6,
            27: 0.44333333E+2, 28: 0.33000000, 29: 0.02255600, 30: 0.00759500,
            31: 0.00061000, 32: 0.0005, 33: 0.81967200, 34: 0.81967200,
            35: 24500.0, 36: 250.0, 37: 0.10204082E-1, 38: 0.12244898E-4,
            39: 0.00006250, 40: 0.00006250, 41: 0.00007625, 42: 1.22, 43: 1.0,
            44: 1.0
        }

    def check_constraints(self, position):
        # Desempaqueta las posiciones
        x1, x2, x3, x4, x5, x6, x7 = position

        # Verifica cada restricción DEB
        constraint1 = self.coefficients[7]*x6**2 + self.coefficients[8]*x1**-1*x3 - self.coefficients[9]*x6 <= 1
        constraint2 = self.coefficients[10]*x1*x3**-1 + self.coefficients[11]*x1*x3**-1*x6 - self.coefficients[12]*x1*x3**-1*x6**2 <= 1
        constraint3 = self.coefficients[13]*x6**2 + self.coefficients[14]*x5 - self.coefficients[15]*x4 - self.coefficients[16]*x6 <= 1
        constraint4 = self.coefficients[17]*x5**-1 + self.coefficients[18]*x5**-1*x6 + self.coefficients[19]*x4*x5**-1 - self.coefficients[20]*x5**-2*x6**2 <= 1
        constraint5 = self.coefficients[21]**x7 + self.coefficients[22]*x2*x3**-1*x4**-1 - self.coefficients[23]*x2*x3**-1 <= 1
        constraint6 = self.coefficients[24]*x7**-1 + self.coefficients[25]*x2*x3**-1*x7**-1 - self.coefficients[26]*x2*x3**-1*x4**-1*x7**-1 <= 1
        constraint7 = self.coefficients[27]*x5**-1 + self.coefficients[28]*x5**-1*x7 <= 1
        constraint8 = self.coefficients[29]*x5 - self.coefficients[30]*x7 <= 1
        constraint9 = self.coefficients[31]*x3 - self.coefficients[32]*x1 <= 1
        constraint10 = self.coefficients[33]*x1*x3**-1 + self.coefficients[34]*x3**-1 <= 1
        constraint11 = self.coefficients[35]*x2*x3**-1*x4**-1 - self.coefficients[36]*x2*x3**-1 <= 1
        constraint12 = self.coefficients[37]*x4 + self.coefficients[38]*x2**-1*x3*x4 <= 1
        constraint13 = self.coefficients[39]*x1*x6 + self.coefficients[40]*x1 - self.coefficients[41]*x3 <= 1
        constraint14 = self.coefficients[42]*x1**-1*x3 + self.coefficients[43]*x1**-1 - self.coefficients[44]*x6 <= 1

        # Devuelve True si todas las restricciones se cumplen, False de lo contrario
        return all([constraint1, constraint2, constraint3, constraint4,
                    constraint5, constraint6, constraint7, constraint8,
                    constraint9, constraint10, constraint11, constraint12,
                    constraint13, constraint14])

    # Método para corregir la posición si no cumple con las restricciones
    def correct_position(self, position):
        # Recorta la posición a los límites inferiores y superiores definidos
        return np.clip(position, self.bounds_lower, self.bounds_upper)
