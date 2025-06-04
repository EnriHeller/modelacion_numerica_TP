import generar_graficos as g
from metodos.euler_explicito import euler_explicito
from metodos.RK2 import RK2
from metodos.solucion_analitica import solucion_analitica_lineal

def comparacion_funciones(casos,t_final,hs,u_0,v_0):
    puntos = 200

    for caso in [1, 2, 3]:
        m = casos[caso]['m']
        c = casos[caso]['c']
        k = casos[caso]['k']
        g.graficar_solucion_analitica(
                lambda t, caso=caso: solucion_analitica_lineal(t, caso), caso, t_final, puntos
        )
        
        # Comparar soluciones numéricas y analítica para cada método
        g.graficar_comparacion_soluciones(
                solucion_analitica_lineal, euler_explicito, hs, m, c, k, u_0, v_0, t_final, caso, puntos
        )
        
        g.graficar_comparacion_soluciones(
                solucion_analitica_lineal, RK2, hs, m, c, k, u_0, v_0, t_final, caso, puntos
        )

def comparacion_errores(casos,t_finales,hs,u_0,v_0):
    for caso in [1, 2, 3]:
        m = casos[caso]['m']
        c = casos[caso]['c']
        k = casos[caso]['k']
        for t_final in t_finales:
            g.graficar_comparacion_h(euler_explicito, hs, m, c, k, u_0, v_0, t_final, f"Euler explícito - t_final={t_final}", caso)
            g.graficar_comparacion_h(RK2, hs, m, c, k, u_0, v_0, t_final, f"RK2- t_final={t_final}", caso)

def main():
    # Definición de los casos
    casos = {
        1: {'m': 1, 'c': 5, 'k': 100},
        2: {'m': 0.1, 'c': 0.55, 'k': 0.625},
        3: {'m': 10, 'c': 10, 'k': 0.5}
    }
    u_0 = 10 ** -2
    v_0 = 1
    hs = [0.1, 0.05, 0.025]
    t_finales = [0.5, 2, 5, 10]

    #comparacion_funciones(casos,10,hs,u_0,v_0)
    comparacion_errores(casos,t_finales,hs,u_0,v_0)

main()
