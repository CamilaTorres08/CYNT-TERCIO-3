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
      
## Función 3
Esta función representa cuando la entrada es 0, tiene como salida 1. De igual manera, cuando la entrada es 1, tiene como salida 0. Haciendo uso de una sola compuerta CNOT y negando la entrada del 'alambre' de arriba para que actue como Uf del agoritmo de Deustch; obtenemos el resultado esperado, una función balanceada.

      circuit = QuantumCircuit(2, 1)
      circuit.x(1)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.barrier()
      circuit.barrier()
      circuit.x(0)
      circuit.cnot(0,1)
      circuit.x(0)
      circuit.barrier()
      circuit.h(0)

      circuit.measure([0], [0])
      
## Función 4
Esta función representa que ambas entradas tienen como salida 1. Para saber cual es la matriz Uf, se niega de la entrada de arriba y se realiza el uso de dos compuerta CNOT, al final, se obtiene el valor esperado, una función constante.

      circuit = QuantumCircuit(2, 1)
      circuit.x(1)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.barrier()
      circuit.barrier()
      circuit.x(0)
      circuit.cnot(0,1)
      circuit.x(0)
      circuit.cnot(0,1)
      circuit.barrier()
      circuit.h(0)

      circuit.measure([0], [0])
      
# Programa algoritmo de Deutsch-Jotza

A continuación se presenta el programa "DeustchJotza" donde a través de la libreria Qiskit, se realiza una simulación del algoritmo de Deustch-Jotza con n = 4, tres funciones balanceadas y una constante.
Tiene como objetivo determinar, de la misma manera que el algoritmo de Deustch, cuando una función es constante o balanceada. Siendo la salida 000...n cuando es constante y balanceada en caso contrario. 

## Como usar
   ### Función 1
   Esta función representa cuando la primera mitad de las entradas van a 0 y la otra mitad a 1. Se hace uso de una compuerta CNOT con la primera entrada y la ultima, para así obtener el resultado esperado, una función balanceada.  
       
      circuit = QuantumCircuit(5, 5)
      circuit.x(4)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.h(4)
      circuit.barrier()
      circuit.barrier()
      circuit.cnot(0,4)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.barrier()
      circuit.measure([0,1,2,3], [0,1,2,3])
    

### Función 2
  Esta función representa las entradas se van intercalando, una mitas va a 0 y otra a 1. Para comprobar que es balanceada, se hace uso de la compuerta CNOT entre la cuarta entrada y la ultima entrada. Así, se comprueba que esta es balanceada. 
  
     circuit = QuantumCircuit(5, 5)
      circuit.x(4)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.h(4)
      circuit.barrier()
      circuit.barrier()
      circuit.cnot(3,4)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.barrier()
      circuit.measure([0,1,2,3], [0,1,2,3])
      
## Función 3
Esta función representa cuando la primera mitad de las entradas van a 1 y la otra mitad a 0. Se hace uso de una compuerta CNOT y la negación con la primera entrada y la ultima, para así obtener el resultado esperado, una función balanceada.  

      circuit = QuantumCircuit(5, 5)
      circuit.x(4)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.h(4)
      circuit.barrier()
      circuit.barrier()
      circuit.x(0)
      circuit.cnot(0,4)
      circuit.x(0)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.barrier()
      circuit.measure([0,1,2,3], [0,1,2,3])
      
## Función 4
Esta función representa cuando todas las entradas van a 0. Para comprobar que es constante, no se usa ninguna compuerta ya que la salida es la misma, así se obtiene el resultado 0000 el cual indica que es constante. 

      circuit = QuantumCircuit(5, 5)
      circuit.x(4)
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.h(4)
      circuit.barrier()
      circuit.barrier()
      
      circuit.barrier()
      circuit.h(0)
      circuit.h(1)
      circuit.h(2)
      circuit.h(3)
      circuit.barrier()
      circuit.measure([0,1,2,3], [0,1,2,3])

## Lenguaje de programación

Python

## Autor

Andrea Camila Torres González
