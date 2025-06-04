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

PASO 4 - Definimos elementos para aplicar RK2

Aproximo numericamente:

u^n = u(t)
v^n = v'(t)

Las formulas de RK2 son:

PASO PREDICTOR:
u^*[n+1] = u^n + h * v^n

v^*[n+1] = v^n + h * (-c v^n - k u^n) / m 

PASO CORRECTOR:

u^{n+1} = u^n + (h/2) * (v^n + v^*[n+1])

v^{n+1} = v^n + (h/2) * (f2(u^n, v^n) + f2(u^*[n+1], v^*[n+1]))

donde f2(u, v) = (-c*v - k*u)/m



PASO 5: Iteramos a partir de condiciones iniciales

- Los valores los elegimos nosotros

CODEAR
"""

"""
Solucion analitica por wolfram:

x(t) = e^(-(5 t)/2) (0.01 cos((5 sqrt(15) t)/2) + 0.105862 sin((5 sqrt(15) t)/2))

"""

def RK2(m, c, k, h, u_0, v_0, t_final, resultado_file="resultados_RK2.txt", caso=None):
    import os
    # Redirigir resultados a la carpeta corridas_numericas/sin_revisar
    base_dir = "corridas_numericas/sin_revisar"
    os.makedirs(base_dir, exist_ok=True)
    resultado_file = os.path.join(base_dir, os.path.basename(resultado_file))

    def f2(u, v, c, k, m):
        return (-c * v - k * u) / m
    n = int(t_final / h)
    u_n = u_0
    v_n = v_0
    with open(resultado_file, "w") as f:
        header = f"{'n':>3} {'t':>8} {'u^n':>12} {'v^n':>12} {'u^(n+1)':>12} {'v^(n+1)':>12} {'y(t)':>14} {'error':>12}"
        f.write(header + "\n")
        for i in range(n):
            t = h * i
            # Predictor
            u_pred = u_n + h * v_n
            v_pred = v_n + h * f2(u_n, v_n, c, k, m)
            # Corrector
            u_n1 = u_n + (h / 2) * (v_n + v_pred)
            v_n1 = v_n + (h / 2) * (f2(u_n, v_n, c, k, m) + f2(u_pred, v_pred, c, k, m))
            y_t = solucion_analitica_lineal(t, caso)
            error = u_n - y_t
            f.write(f"{i:3d} {t:8.4f} {u_n:12.6f} {v_n:12.6f} {u_n1:12.6f} {v_n1:12.6f} {y_t:14.6f} {error:12.6e}\n")
            u_n = u_n1
            v_n = v_n1


