
1
ANÁLISIS NUMÉRICO I (75.12 – 95.04) 
MÉTODOS MATEMÁTICOS Y NUMÉRICOS (95.13) 
MODELACIÓN NUMÉRICA (CB051) 
FACULTAD DE INGENIERÍA – UNIVERSIDAD DE BUENOS AIRES 
 
TRABAJO PRÁCTICO 
1er cuatrimestre 2025 
 
Resolución numérica de problemas de valores iniciales 
Análisis numérico de un sistema vibratorio lineal y no lineal 
 
 
Introducción 
En muchas ramas de la ingeniería es fundamental comprender cómo responde un sistema físico ante 
perturbaciones  mecánicas.  Un  ejemplo  clásico  es  el  comportamiento  de  una  estructura  sometida  a  una  fuerza 
inicial, como ocurre en puentes, edificios o componentes mecánicos que vibran tras un impacto o desplazamiento. 
El  modelo  matemático  más  básico  que  describe  esta  situación  es  el  sistema  masa-resorte-amortiguador,  que 
permite  estudiar  el  movimiento  oscilatorio  de  un  cuerpo  sometido  a  una  fuerza  restauradora  (resorte)  y  una 
fuerza disipativa (amortiguador). Este sistema puede extenderse fácilmente a casos más realistas donde aparecen 
no  linealidades  en  el  resorte,  lo  que  genera  fenómenos  más  complejos,  imposibles  de  analizar  con  métodos 
analíticos clásicos. 
Este  trabajo  práctico  propone  la  resolución  numérica  de  un  sistema  masa-resorte-amortiguador  lineal,  con 
validación frente a la solución exacta, y luego el análisis de un caso no lineal mediante simulación computacional. 
 
Modelo físico 
Sistema lineal (modelo base): 
𝑚𝑥′′(𝑡)+𝑐𝑥′(𝑡)+𝑘𝑥(𝑡)=0 
Sistema no lineal (extensión con resorte no lineal): 
𝑚𝑥′′(𝑡)+𝑐𝑥′(𝑡)+𝑘𝑥(𝑡)+𝛼𝑥(𝑡)3 =0 
Unidades y órdenes de magnitud sugeridos: 
Variable/Parámetro Significado Orden típico 
x(t) Desplazamiento de la masa 10−2 a 10−1 m 
m Masa del cuerpo 0.1 a 10 kg 
c Coeficiente de amortiguamiento 0.1 a 10 Ns/m 
k Constante elástica del resorte 10 a 1000 N/m 
α Coef. de rigidez no lineal (Duffing) ±104 a ±106 N/m³ 
t Tiempo 0 a 10 s 
Objetivos y consignas 
 
Parte 1 – Análisis del sistema lineal 
Reescribir el sistema de segundo orden como un sistema de dos ecuaciones de primer orden. Implementar dos 
métodos numéricos para resolver el sistema: Euler explícito y otro método de mayor orden. 
Resolver el sistema para diferentes valores del coeficiente de amortiguamiento relativo 𝜁 = 𝑐
2√𝑘𝑚 : 
subamortiguado (ζ < 1), críticamente amortiguado (ζ = 1) y sobreamortiguado (ζ > 1). 
Calcular  y  graficar  la  solución  analítica  correspondiente  en  cada  caso.  Comparar  la  solución  numérica  con  la 
solución analítica gráficamente y mediante el cálculo del error. 
Analizar el efecto del tamaño de paso h sobre la precisión y la estabilidad de los métodos utilizados. 
 
Parte 2 – Incorporación de no linealidad y análisis del oscilador de Duffing 
Modificar el modelo para incluir una rigidez no lineal mediante el término αx(t)3. 
Resolver numéricamente el nuevo sistema utilizando el mismo esquema que en la parte 1 (no se requiere solución 
analítica). Analizar el comportamiento cualitativo de la solución: oscilaciones periódicas, amortiguadas, 
amplificadas o caóticas. Analizar cómo varía la respuesta según el signo y valor de α. Comparar con el caso lineal 
de la parte 1. 
Investigar brevemente el modelo del oscilador de Duffing: 
¿Dónde aparece en la práctica? 
¿Por qué es importante como modelo no lineal? 
¿Qué tipo de comportamiento puede presentar? 
Incluir una referencia bibliográfica (libro, artículo o fuente académica) que lo describa. 