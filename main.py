import generar_graficos as g
from metodos.euler_explicito import euler_explicito
from metodos.RK2 import RK2


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
    m = 10
    c = 10
    k = 0.5
    
    ##CONSTANTES
    u_0 = 10 **-2
    v_0= 1
    hs = [0.1, 0.05, 0.025]
    t_final_1 = 0.5
    t_final_2 = 2


    ## EJECUCION

    #Solucion analitica lineal
    #g.graficar_solucion_analitica(e.solucion_analitica, 10, 200)


    # EULER EXPLICITO & RK2

    #metodo, nombre_metodo = euler_explicito,"Euler Explicito"
    metodo, nombre_metodo = RK2,"RK2"

    g.graficar_comparacion_h(metodo, hs, m, c, k, u_0, v_0, t_final_1, nombre_metodo)
    g.graficar_comparacion_h(metodo, hs, m, c, k, u_0, v_0, t_final_2, nombre_metodo)

main()
