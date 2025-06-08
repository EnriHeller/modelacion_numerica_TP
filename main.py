import generar_graficos as g
from metodos.euler_explicito import euler_explicito
from metodos.RK2 import RK2
from metodos.solucion_analitica import solucion_analitica_lineal
from parte2.euler_no_lineal import euler_explicito_no_lineal, graficar_no_lineal_multi_h

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

def euler_no_lineal_modular(casos, caso, hs, t_final, u_0, v_0, alpha):
    
    resultados = {}
    m = casos[caso]['m']
    c = casos[caso]['c']
    k = casos[caso]['k']
    for h in hs:
        resultado_file = f"parte2/resultados_euler_no_lineal_caso{caso}_h{h}_alpha_{str(alpha).replace('.', 'p').replace('-', 'm')}.txt"
        ts, us = euler_explicito_no_lineal(m, c, k, h, u_0, v_0, t_final, alpha, resultado_file)
        resultados[h] = (ts, us)
    nombre_grafico = f"parte2/grafico_no_lineal_caso{caso}_alpha_{str(alpha).replace('.', 'p').replace('-', 'm')}.png"
    graficar_no_lineal_multi_h(resultados, alpha, caso, nombre_grafico)

def main():
    # Definición de los casos
    casos = {
        1: {'m': 1, 'c': 5, 'k': 100},
        2: {'m': 0.1, 'c': 0.55, 'k': 0.625},
        3: {'m': 10, 'c': 10, 'k': 0.5}
    }
    u_0 = 10 ** -2
    v_0 = 1
    """ hs = [0.1, 0.05, 0.025] """ #hs de c1
    #hs = [1.05,2.1,4.2] #hs de c2
    hs = [0.5,1,0.25] #hs de c2

    t_finales = [0.5, 2, 5, 10]

    #comparacion_funciones(casos,10,hs,u_0,v_0)
    #comparacion_errores(casos,t_finales,hs,u_0,v_0)
    # --- NUEVO: Euler explícito no lineal modularizado ---
    alpha = -10  # Cambia este valor para probar distintos alphas
    caso = 2
    t_final = 5
    euler_no_lineal_modular(casos, caso, hs, t_final, u_0, v_0, alpha)

main()
