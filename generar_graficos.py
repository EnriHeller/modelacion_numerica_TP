import matplotlib.pyplot as plt
import numpy as np
import os

def graficar_comparacion_h(metodo, hs, m, c, k, u_0, v_0, t_final, nombre_metodo="", caso=None): 
    plt.figure(figsize=(12,6))
    for h in hs:
        resultado_file = f"resultados_{nombre_metodo.replace(' ', '_').lower()}_h{h}_caso{caso}.txt"
        resultado_file = os.path.join("corridas_numericas/sin_revisar", os.path.basename(resultado_file))
        metodo(m, c, k, h, u_0, v_0, t_final, resultado_file, caso=caso)
        ts = []
        errores = []
        with open(resultado_file) as f:
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
        plt.plot(ts, errores, 'o--', label=f'Error global {nombre_metodo} h={h}', markersize=6)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('Error global $E^n = u^n - y(t^n)$', fontsize=14)
    plt.title(f'Comparación de error global para distintos h ({nombre_metodo}, caso {caso})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(f"grafico_error_{nombre_metodo}_caso{caso}.png")  # Guarda el gráfico
    plt.show()
    plt.close()

def graficar_solucion_analitica(solucion_analitica, caso, t_final, n_puntos=200):
    ts = np.linspace(0, t_final, n_puntos)
    us = [solucion_analitica(t, caso) for t in ts]
    plt.figure(figsize=(10,5))
    plt.plot(ts, us, label=f'Solución analítica caso {caso}', color='black', linewidth=2)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('y(t)', fontsize=14)
    plt.title(f'Solución analítica (caso {caso})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(f"grafico_analitica_caso{caso}.png")  # Guarda el gráfico
    plt.show()
    plt.close()

def graficar_comparacion_soluciones(solucion_analitica, metodo, hs, m, c, k, u_0, v_0, t_final, caso, n_puntos=200, ylim=None, xlim=None):
    ts = np.linspace(0, t_final, n_puntos)
    us = [solucion_analitica(t, caso) for t in ts]
    plt.figure(figsize=(10,5))
    plt.plot(ts, us, label='Solución analítica', color='black', linewidth=2)
    # Graficar la solución aproximada para cada h
    for h in hs:
        resultado_file = f"resultados_{metodo.__name__.replace(' ', '_').lower()}_h{h}_caso{caso}.txt"
        resultado_file = os.path.join("corridas_numericas/sin_revisar", os.path.basename(resultado_file))
        metodo(m, c, k, h, u_0, v_0, t_final, resultado_file, caso=caso)
        ts_aprox = []
        us_aprox = []
        with open(resultado_file) as f:
            next(f)
            for line in f:
                if line.strip() == '':
                    continue
                parts = line.split()
                t_aprox = float(parts[1])
                u_n = float(parts[2])
                ts_aprox.append(t_aprox)
                us_aprox.append(u_n)
        plt.plot(ts_aprox, us_aprox, marker='o', linestyle='--', label=f'Sol. numérica h={h}', markersize=2.5)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('y(t)', fontsize=14)
    plt.title(f'Solución analítica y numérica (caso {caso}, método {metodo.__name__})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    if ylim is not None:
        plt.ylim(ylim)
    if xlim is not None:
        plt.xlim(xlim)
    plt.savefig(f"grafico_comparacion_{metodo.__name__}_caso{caso}.png")  # Guarda el gráfico
    plt.show()
    plt.close()






