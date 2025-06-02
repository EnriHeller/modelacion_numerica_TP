import math


"""
Sistema lineal (modelo base):
m*x''(t) + c*x'(t) + k*x(t) = 0

PASO 1 - Aplicamos cambio de variables:

x(t) = x1(t)
x'(t) = x2(t)

-> x1'(t) = x2(t) 
-> x2'(t) = x''(t)

PASO 2 - Despejamos derivada segunda de la ecuación original

x''(t) = [-c*x2(t) - k*x1(t)]/m = f2(t,x1,x2)

PASO 3 - Reescribimos EDO a partir de nuestras nuevas variables.

-> x1'(t) = x2(t) = f1(t,x1,x2)
-> x2'(t) = [-c*x2(t) - k*x1(t)]/m = f2(t,x1,x2)

PASO 4 - Definimos elementos para aplicar Euler explicito

Aproximo numericamente:

u1^n = x1(t)
u2^n = x2(t)

Las formulas de Euler Explicito son:

u1^[n+1] = u1^n + h * u2^n
u2^(n+1) = u2^n + h * (-c u2^n - k u1^n) / m

PASO 5: Iteramos a partir de condiciones iniciales

- Los valores los elegimos nosotros

CODEAR:
"""

"""
Solucion analitica por wolfram:

x(t) = e^(-(5 t)/2) (0.01 cos((5 sqrt(15) t)/2) + 0.105862 sin((5 sqrt(15) t)/2))

"""


def solucion_analitica(t):
        return math.exp(-2.5 * t) * (0.01 * math.cos(5 * math.sqrt(15) / 2 * t) + 0.105862 * math.sin(5 * math.sqrt(15) / 2 * t))

def euler_explicito(m, c, k, h,u_0,v_0, t_final):

    n = int(t_final/h)
    u_n = u_0
    v_n= v_0

    with open("resultados_euler.txt", "w") as f:
        header = f"{'n':>3} {'t':>8} {'u^n':>12} {'v^n':>12} {'u^(n+1)':>12} {'v^(n+1)':>12} {'y(t)':>14} {'error':>12}"
        f.write(header + "\n")
        for i in range(n):
            t = h * i
            u_n1 = u_n + h * v_n
            v_n1 = v_n + h / m * (-c * v_n - k * u_n)
            y_t = solucion_analitica(t)
            error = abs(u_n - y_t)
            f.write(f"{i:3d} {t:8.4f} {u_n:12.6f} {v_n:12.6f} {u_n1:12.6f} {v_n1:12.6f} {y_t:14.6f} {error:12.6e}\n")
            u_n = u_n1
            v_n = v_n1


