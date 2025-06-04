import math

def solucion_analitica_lineal(t,caso):

        if caso == 1:
                return math.exp(-2.5 * t) * (0.01 * math.cos(5 * math.sqrt(15) / 2 * t) + 0.105862 * math.sin(5 * math.sqrt(15) / 2 * t))
        elif caso == 2:
                 #-0.443438 e^(-3.89564 t) + 0.453438 e^(-1.60436 t)
                return -0.443438 * math.exp(-3.89564 * t) + 0.453438 * math.exp(-1.60436 * t)

        elif caso == 3:
                #-1.11862 e^(-0.947214 t) + 1.12862 e^(-0.0527864 t)
                return -1.11862 * math.exp(-0.947214 * t) + 1.12862 * math.exp(-0.0527864 * t)


def solucion_analitica_no_lineal(t):
        pass