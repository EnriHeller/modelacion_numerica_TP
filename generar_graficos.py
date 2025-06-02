import matplotlib.pyplot as plt


def graficar_comparacion_h(metodo, hs, m, c, k, u_0, v_0, t_final, nombre_metodo=""): 
    plt.figure(figsize=(12,6))
    for h in hs:
        # Usar un archivo de resultados diferente para cada h y método
        resultado_file = f"resultados_{nombre_metodo.replace(' ', '_').lower()}_h{h}.txt"
        metodo(m, c, k, h, u_0, v_0, t_final, resultado_file)
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
    plt.title(f'Comparación de error global para distintos h ({nombre_metodo})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()





