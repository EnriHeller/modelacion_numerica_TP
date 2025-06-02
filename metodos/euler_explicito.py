from metodos.solucion_analitica import solucion_analitica_lineal

"""
Sistema lineal (modelo base):
m*x''(t) + c*x'(t) + k*x(t) = 0

PASO 1 - Aplicamos cambio de variables:

u(t) = x(t)
v(t) = x'(t)

-> u'(t) = v(t)
-> v'(t) = x''(t)

PASO 2 - Despejamos derivada segunda de la ecuación original

x''(t) = [-c*v(t) - k*u(t)]/m = f2(t,u,v)

PASO 3 - Reescribimos EDO a partir de nuestras nuevas variables.

-> u'(t) = v(t) = f1(t,u,v)
-> v'(t) = [-c*v(t) - k*u(t)]/m = f2(t,u,v)

PASO 4 - Definimos elementos para aplicar Euler explicito

Aproximo numericamente:

u^n = u(t)
v^n = v(t)

Las formulas de Euler Explicito son:

u^[n+1] = u^n + h * v^n
v^(n+1) = v^n + h * (-c v^n - k u^n) / m

PASO 5: Iteramos a partir de condiciones iniciales

- Los valores los elegimos nosotros

CODEAR:
"""

"""
Solucion analitica por wolfram:

x(t) = e^(-(5 t)/2) (0.01 cos((5 sqrt(15) t)/2) + 0.105862 sin((5 sqrt(15) t)/2))

"""

def euler_explicito(m, c, k, h, u_0, v_0, t_final, resultado_file="resultados_euler.txt"):

    n = int(t_final/h)
    u_n = u_0
    v_n= v_0

    with open(resultado_file, "w") as f:
        header = f"{'n':>3} {'t':>8} {'u^n':>12} {'v^n':>12} {'u^(n+1)':>12} {'v^(n+1)':>12} {'y(t)':>14} {'error':>12}"
        f.write(header + "\n")
        for i in range(n):
            t = h * i
            u_n1 = u_n + h * v_n
            v_n1 = v_n + h / m * (-c * v_n - k * u_n)
            y_t = solucion_analitica_lineal(t)
            error = u_n - y_t
            f.write(f"{i:3d} {t:8.4f} {u_n:12.6f} {v_n:12.6f} {u_n1:12.6f} {v_n1:12.6f} {y_t:14.6f} {error:12.6e}\n")
            u_n = u_n1
            v_n = v_n1


