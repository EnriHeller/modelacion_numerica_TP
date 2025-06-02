import matplotlib.pyplot as plt
from euler_explicito import euler_explicito, solucion_analitica
import numpy as np

def leer_resultados(filename):
    ts = []
    us = []
    with open(filename) as f:
        next(f)
        for line in f:
            if line.strip() == '':
                continue
            parts = line.split()
            ts.append(float(parts[1]))
            us.append(float(parts[2]))
    return np.array(ts), np.array(us)

def graficar_comparacion_h(hs, m, c, k, u_0, v_0, t_final):
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
            
    # Solución numérica vs analítica
    """plt.figure(figsize=(12,6))
    plt.plot(ts, u_num, label='Solución numérica (Euler)', marker='o', markersize=7, linewidth=2)
    plt.plot(ts, u_ana, label='Solución analítica', linestyle='--', linewidth=2)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('u(t)', fontsize=14)
    plt.title('Comparación: Solución numérica vs. analítica', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()"""
    
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

    """
    # Error absoluto
    plt.figure(figsize=(12,6))
    plt.plot(ts, errores, label='Error absoluto |u_num - u_ana|', color='red', linewidth=2, marker='o', markersize=7)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('Error absoluto', fontsize=14)
    plt.title('Error absoluto entre solución numérica y analítica', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()
    """

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



