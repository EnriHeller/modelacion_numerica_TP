
import generar_graficos as g


def main():

    #Solucion analitica
    #g.graficar_solucion_analitica(e.solucion_analitica, 10, 200)


    # EULER EXPLICITO & RK2

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

    

    u_0 = 10 **-2
    v_0= 1

    hs = [0.1, 0.05, 0.025]

    t_final_1 = 0.5
    t_final_2 = 2

    #g.graficar_euler_comparacion_h(hs,m,c,k,u_0,v_0,t_final_1)
    #g.graficar_euler_comparacion_h(hs,m,c,k,u_0,v_0,t_final_2)

    g.graficar_RK2_comparacion_h(hs,m,c,k,u_0,v_0,t_final_1)
    g.graficar_RK2_comparacion_h(hs,m,c,k,u_0,v_0,t_final_2)


main()
