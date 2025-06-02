import matplotlib.pyplot as plt
import numpy as np

from metodos.euler_explicito import euler_explicito


def graficar_euler_comparacion_h(hs, m, c, k, u_0, v_0, t_final):
    plt.figure(figsize=(12,6))
    for h in hs:
        euler_explicito(m, c, k, h, u_0, v_0, t_final)
        ts = []
        errores = []
        with open("resultados_euler.txt") as f:
            next(f)
            for line in f:
                if line.strip() == '':
                    continue
                parts = line.split()
                t = float(parts[1])
                u_n = float(parts[2])
                u_analitica = float(parts[6])
                error = u_n - u_analitica
                ts.append(t)
                errores.append(error)
        plt.plot(ts, errores, 'o--', label=f'Error global h={h}', markersize=6)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('Error global $E^n = u^n - y(t^n)$', fontsize=14)
    plt.title('Comparación de error global para distintos h', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def graficar_euler_error():
    ts = []
    u_num = []
    u_ana = []
    errores = []
    error_global = []
    max_error = 0
    with open("resultados_euler.txt") as f:
        next(f)  
        for line in f:
            if line.strip() == '':
                continue
            parts = line.split()
            t = float(parts[1])
            u_n = float(parts[2])
            u_analitica = float(parts[6])
            error = float(parts[7])
            ts.append(t)
            u_num.append(u_n)
            u_ana.append(u_analitica)
            errores.append(error)
            max_error = max(max_error, error)
            error_global.append(max_error)
        
    
    # Solución numérica vs analítica (puntos unidos por línea entrecortada)
    plt.figure(figsize=(12,6))
    plt.plot(ts, u_ana, label='Solución analítica', color='black', linewidth=2)
    plt.plot(ts, u_num, 'o--', label='Solución numérica (Euler)', color='blue', markersize=7, linewidth=2)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('u(t)', fontsize=14)
    plt.title('Comparación: Solución numérica (puntos y línea entrecortada) vs. analítica', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

    # Error global solo con puntos
    plt.figure(figsize=(12,6))
    plt.plot(ts, error_global, 'o', label='Error global hasta t', color='blue', markersize=7)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('Error global', fontsize=14)
    plt.title('Error global respecto al tiempo', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def graficar_solucion_analitica(solucion_analitica, t_final, n_puntos=200):
    ts = np.linspace(0, t_final, n_puntos)
    us = [solucion_analitica(t) for t in ts]
    plt.figure(figsize=(10,5))
    plt.plot(ts, us, label='Solución analítica', color='black', linewidth=2)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('y(t)', fontsize=14)
    plt.title('Solución analítica', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def graficar_RK2_comparacion_h(hs, m, c, k, u_0, v_0, t_final):
    plt.figure(figsize=(12,6))
    from metodos.RK2 import RK2
    for h in hs:
        RK2(m, c, k, h, u_0, v_0, t_final)
        ts = []
        errores = []
        with open("resultados_RK2.txt") as f:
            next(f)
            for line in f:
                if line.strip() == '':
                    continue
                parts = line.split()
                t = float(parts[1])
                u_n = float(parts[2])
                u_analitica = float(parts[6])
                error = u_n - u_analitica
                ts.append(t)
                errores.append(error)
        plt.plot(ts, errores, 'o--', label=f'Error global RK2 h={h}', markersize=6)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('Error global $E^n = u^n - y(t^n)$', fontsize=14)
    plt.title('Comparación de error global RK2 para distintos h', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()



