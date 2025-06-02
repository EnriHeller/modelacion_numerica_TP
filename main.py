
import generar_graficos as g

def main():

    # EULER EXPLICITO
    ## Z < 1 -> Z = 1/4
    """

    m = 1
    c = 5
    k = 100
    u_0 = 10 **-2
    v_0= 1
    t_final=2

    hs = [0.1, 0.05, 0.025]

    g.graficar_comparacion_h(hs,m,c,k,u_0,v_0,t_final)

    """
    ## Z = 1

    """
    m = 0.1
    c = 0.55
    k = 0.625
    u_0 = 10 **-2
    v_0= 1
    t_final=0.5

    hs = [0.1, 0.05, 0.025]

    g.graficar_comparacion_h(hs,m,c,k,u_0,v_0,t_final)
    """

    ## Z > 1 -> Z = sqrt(5)

    m = 10
    c = 10
    k = 0.5
    u_0 = 10 **-2
    v_0= 1
    t_final=2

    hs = [0.1, 0.05, 0.025]

    g.graficar_comparacion_h(hs,m,c,k,u_0,v_0,t_final)

main()
