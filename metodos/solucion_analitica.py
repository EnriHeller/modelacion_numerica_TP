import math

def solucion_analitica_lineal(t):
        return math.exp(-2.5 * t) * (0.01 * math.cos(5 * math.sqrt(15) / 2 * t) + 0.105862 * math.sin(5 * math.sqrt(15) / 2 * t))

def solucion_analitica_no_lineal(t):
        pass