import generar_graficos as g
from metodos.euler_explicito import euler_explicito
from metodos.RK2 import RK2
from metodos.solucion_analitica import solucion_analitica_lineal

def comparacion_funciones(casos, t_final, hs, u_0, v_0, caso, metodo, nombre_metodo, alpha=0.0):
    puntos = 200
    m = casos[caso]['m']
    c = casos[caso]['c']
    k = casos[caso]['k']
    g.graficar_solucion_analitica(
        lambda t, caso=caso: solucion_analitica_lineal(t, caso), caso, t_final, puntos
    )
    # Construir sufijo seguro para el nombre del archivo según alpha
    alpha_str = f"alpha_{str(alpha).replace('.', 'p').replace('-', 'm')}"
    # Comparar soluciones numéricas y analítica solo para el método elegido
    g.graficar_comparacion_soluciones(
        solucion_analitica_lineal, 
        lambda m, c, k, h, u_0, v_0, t_final, resultado_file, caso: metodo(
            m, c, k, h, u_0, v_0, t_final, 
            resultado_file.replace(".txt", f"_{alpha_str}.txt"), caso, alpha
        ),
        hs, m, c, k, u_0, v_0, t_final, caso, puntos
    )

def comparacion_errores(casos, t_finales, hs, u_0, v_0, caso, metodo, nombre_metodo, alpha=0.0):
    m = casos[caso]['m']
    c = casos[caso]['c']
    k = casos[caso]['k']
    for t_final in t_finales:
        g.graficar_comparacion_h(
            lambda m, c, k, h, u_0, v_0, t_final, resultado_file, caso: metodo(m, c, k, h, u_0, v_0, t_final, resultado_file, caso, alpha),
            hs, m, c, k, u_0, v_0, t_final, f"{nombre_metodo} - t_final={t_final}", caso
        )

def main():
    # Definición de los casos
    casos = {
        1: {'m': 1, 'c': 5, 'k': 100},
        2: {'m': 0.1, 'c': 0.55, 'k': 0.625},
        3: {'m': 10, 'c': 10, 'k': 0.5}
    }
    u_0 = 10 ** -2
    v_0 = 1
    hs = [0.025, 0.05, 0.1]
    t_finales = [0.5, 2, 5, 10]
    # Selección del caso y método
    caso = 1  # Cambia este valor para elegir el caso a graficar (1, 2 o 3)
    metodo_id = 0  # 0 para Euler explícito, 1 para RK2
    alpha = -1.0  # Cambia este valor para activar la no linealidad

    if metodo_id == 0:
        metodo = euler_explicito
        nombre_metodo = "Euler explícito"
    elif metodo_id == 1:
        metodo = RK2
        nombre_metodo = "RK2"
    else:
        raise ValueError("Método no reconocido. Usa 0 (Euler) o 1 (RK2).")

    comparacion_funciones(casos, 1, hs, u_0, v_0, caso, metodo, nombre_metodo, alpha)
    #comparacion_errores(casos, t_finales, hs, u_0, v_0, caso, metodo, nombre_metodo, alpha)

main()
