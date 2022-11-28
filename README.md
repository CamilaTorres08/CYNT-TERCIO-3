# Programa algoritmo de Deutsch

A continuación se presenta el programa "Deustch" donde a través de la libreria Qiskit, se realiza una simulación del algoritmo de Deustch usando las cuatro funciones primordiales de este algoritmo.
Tiene como objetivo determinar cuando una función es constante o balanceada. Siendo  la salida 0 cuando es constante y balanceada en caso contrario. 

## Como usar
   ### Función 1
   Esta función representa cuando las dos entradas tiene como salida 0, para demostrar que esta es constante, se hace uso de doble compuerta CNOT para que actue como Uf y se arma el circuito de acuerdo al algoritmo de Deustch. 
       
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


      circuit.measure([0], [0])
    

### Función 2
  Esta función representa cuando la entrada es 0, tiene como salida 0. De igual manera, cuando la entrada es 1, tiene como salida 1. Haciendo uso de una sola compuerta CNOT para que actue como Uf del agoritmo de Deustch; obtenemos el resultado esperado, una función balanceada.
  
     ```
     circuit = QuantumCircuit(2, 1)
      circuit.x(1)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.barrier()
      circuit.barrier()
      circuit.cnot(0,1)
      circuit.barrier()
      circuit.h(0)

      circuit.measure([0], [0])
      '''
   
  



## Lenguaje de programación

Python

## Autor

Andrea Camila Torres González
