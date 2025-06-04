import generar_graficos as g
from metodos.euler_explicito import euler_explicito
from metodos.RK2 import RK2
from metodos.solucion_analitica import solucion_analitica_lineal


def main():

    ## Z < 1 -> Z = 1/4

    """
    m = 1
    c = 5
    k = 100
    """
    
    ## Z = 1
    """
    m = 0.1
    c = 0.55
    k = 0.625
    """

    ## Z > 1 -> Z = sqrt(5)
    """
    m = 10
    c = 10
    k = 0.5
    """
    
    ##CONSTANTES
    u_0 = 10 **-2
    v_0= 1
    hs = [0.1, 0.05, 0.025]
    t_final_1 = 0.5
    t_final_2 = 2


    ## EJECUCION

    

    # EULER EXPLICITO & RK2
    # Ejemplo para Z > 1 -> Z = sqrt(5)
    m = 10
    c = 10
    k = 0.5


    ##Constantes
    u_0 = 10 **-2
    v_0 = 1
    hs = [0.1, 0.05, 0.025]
    t_final_1 = 0.5
    t_final_2 = 2


    #Solucion analitica lineal
    g.graficar_solucion_analitica(solucion_analitica_lineal, 10, 200)
    g.graficar_comparacion_h(euler_explicito, hs, m, c, k, u_0, v_0, t_final_1, "Euler explícito")

    g.graficar_comparacion_h(RK2, hs, m, c, k, u_0, v_0, t_final_2, "RK2")

main()
