import numpy as np
import matplotlib.pyplot as plt
import os

def euler_explicito_no_lineal(m, c, k, h, u_0, v_0, t_final, alpha, resultado_file="resultados_euler_no_lineal.txt"):
    base_dir = os.path.dirname(resultado_file)
    if base_dir:
        os.makedirs(base_dir, exist_ok=True)
    n = int(t_final / h)
    u_n = u_0
    v_n = v_0
    ts = [0]
    us = [u_0]
    with open(resultado_file, "w") as f:
        header = f"{'n':>3} {'t':>8} {'u^n':>12} {'v^n':>12} {'u^(n+1)':>12} {'v^(n+1)':>12}"
        f.write(header + "\n")
        for i in range(n):
            t = h * i
            u_n1 = u_n + h * v_n
            v_n1 = v_n + h / m * (-c * v_n - k * u_n - alpha * u_n**3)
            f.write(f"{i:3d} {t:8.4f} {u_n:12.6f} {v_n:12.6f} {u_n1:12.6f} {v_n1:12.6f}\n")
            u_n = u_n1
            v_n = v_n1
            ts.append(t + h)
            us.append(u_n)
    return np.array(ts), np.array(us)

def graficar_no_lineal(ts, us, alpha, caso, nombre_archivo="grafico_no_lineal.png"):
    plt.figure(figsize=(10,5))
    plt.plot(ts, us, label=f"Euler explícito no lineal (alpha={alpha})", color="tab:blue")
    plt.xlabel('t', fontsize=14)
    plt.ylabel('x(t)', fontsize=14)
    plt.title(f'Solución numérica no lineal (caso {caso}, alpha={alpha})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    #plt.ylim(0,0.10)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.show()
    plt.close()

def graficar_no_lineal_multi_h(resultados, alpha, caso, nombre_archivo="grafico_no_lineal_multi_h.png"):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,5))
    for h, (ts, us) in resultados.items():
        plt.plot(ts, us, label=f"h={h}")
    plt.xlabel('t', fontsize=14)
    plt.ylabel('x(t)', fontsize=14)
    plt.title(f'Solución numérica no lineal (caso {caso}, alpha={alpha})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim([-6, 6]) 
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.show()
    plt.close()
