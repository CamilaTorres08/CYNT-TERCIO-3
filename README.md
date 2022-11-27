# Programa algoritmo de Deutsch

A continuación se presenta el programa "Deustch" donde a través de la libreria Qiskit, se realiza una simulación del algoritmo de Deustch usando las cuatro funciones primordiales de este algoritmo.
Tiene como objetivo determinar cuando una función es constante o balanceada. Siendo  la salida 0 cuando es constante y balanceada en caso contrario. 

## Como usar
   ### Función 1
       Esta función representa cuando las dos entradas tiene como salida 0, para demostrar que esta es constante, se hace uso de sobre compuerta CNOT para que actue como Uf y se arma el circuito de acuerdo al algoritmo de Deustch. 
       
      ```
      circuit = QuantumCircuit(2, 1)
      circuit.x(1)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.barrier()
      circuit.barrier()
      circuit.cnot(0,1)
      circuit.cnot(0,1)
      circuit.barrier()
      circuit.h(0)
      ```


circuit.measure([0], [0])
    

<!--endsec-->

<!--sec data-title="Prompt: Windows" data-id="windows_prompt2" data-collapse=true ces-->

**Programa 'teoría cuantica':
  'El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador permite especificar el número de posiciones y un vector ket de estado asignando las amplitudes.'. Este simulador,antes de realizar los respectivos calculos, verifica que el vector este normalizado, si no, lo normaliza y calcula la probabilidad de que esté en cierta posición, si se desea saber la amplitud, este, contiene una función que la calcula y le retorna el valor.
  
  `print(probabilidad([(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)],7))`
  
  `print(amplitud([(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]))`
  
**Programa 'cynt':
Esta función realiza varias funciones, puede calcular el valor esperado, la varianza, los valores propios, vectores propios y la probabilidad de que el sistema transite a un vector propio. 

Si se desea usar la función para calcular la probabilidad (probabilidad_sistema_eigenvalue) o la función para valores y vectores propios (valores__vectores_propios()), a compración de los demás ejercicios, no es necesario colocar tuplas ya que se hace uso de la libreria numpy. si escribe un complejo, ponga 'j' en lugar de la 'i'. 

para saber los valores y vectores propios, antes debe asignarle a dos variables la función valores__vectores_propios(matriz) y luego llamar a print para imprimir lo que desea visualizar usando el nombre de las dos variables que definió.
 
  `print(valor_esperado([[(0,0),(0,-1)],[(0,1),(0,0)]],[(1/math.sqrt(2),0),(0,1/math.sqrt(2))]))`
  
  `print(varianza([[(0,0),(0,-1)],[(0,1),(0,0)]],[(1/math.sqrt(2),0),(0,1/math.sqrt(2))]))`
  
  `valor,vector = valores__vectores_propios([[0,1],[1,0]])
  print(vector)`
  
  `print(probabilidad_sistema_eigenvalue([[-1,-1j],[1j,1]],[1/2,1/2]))`
  
**programa 'dinamica':
  Este programa hace la verificación de que las matrices sean unitarias (ejercicio 4.4.1) y, asi mismo, puede calcular el estado final a partir de un estado inicial usando la función 'dinamica (matriz,vector,clicks)' en esta, debe pasarle 3 parámetros (matriz,vector incial, clicks) ya que a través de una matriz y un vector inicial, se calcula la probabilidad de que esté en ciertas posiciones después de cierta cantidad de clicks.
  
 `print(unitaria([[(0,0),(1,0)],[(1,0),(0,0)]]))`
 
 `print(dinamica([[(0,0),(1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0)],[(0,1/math.sqrt(2)),(0,0),(0,0),(1/math.sqrt(2),0)],[(1/math.sqrt(2),0),(0,0),(0,0),(0,1/math.sqrt(2))],[(0,0),(1/math.sqrt(2),0),(-1/math.sqrt(2),0),(0,0)]],[(1,0),(0,0),(0,0),(0,0)],3)) `


## Lenguaje de programación

Python

## Autor

Andrea Camila Torres González
