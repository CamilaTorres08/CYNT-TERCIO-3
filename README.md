# Programa algoritmo de Deutsch

A continuación se presenta el programa "Deustch" donde a través de la libreria Qiskit, se realiza una simulación del algoritmo de Deustch usando las cuatro funciones primordiales de este algoritmo.
Tiene como objetivo determinar cuando una función es constante o balanceada. Siendo  la salida 0 cuando es constante y balanceada en caso contrario. 

## Como usar
   ### Función 1
   Esta función representa cuando las dos entradas tiene como salida 0, para demostrar que esta es constante, se hace uso de doble compuerta CNOT para que actue como Uf y se arma el circuito de acuerdo al algoritmo de Deustch. 
   
   ![image](https://user-images.githubusercontent.com/111332434/204168552-370c5785-1552-4923-b50f-f1161de105d1.png)
   ![image](https://user-images.githubusercontent.com/111332434/204168594-051ae065-fd2b-48dd-9205-d82beeef8f38.png)
   
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
  ![image](https://user-images.githubusercontent.com/111332434/204168642-bbf0db9f-f961-4207-aa4c-f126ff6eeef3.png)
![image](https://user-images.githubusercontent.com/111332434/204168645-50339aca-a0fa-4cde-a1d0-bc28c4b3c3e5.png)
  
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
![image](https://user-images.githubusercontent.com/111332434/204168672-706c8d2b-7389-4bb6-ac5f-1ef6c82206c5.png)
![image](https://user-images.githubusercontent.com/111332434/204168678-696ff4ea-ce92-428c-87d9-fb50fc9eb7b3.png)

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
![image](https://user-images.githubusercontent.com/111332434/204168689-c4623902-2386-48bf-b0f2-0d155cd761bf.png)
![image](https://user-images.githubusercontent.com/111332434/204168696-1fab2d52-74c0-4731-b18d-27668db160c8.png)

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
   ![image](https://user-images.githubusercontent.com/111332434/204168714-3d5e27b5-2c9c-4503-b2fc-332e410cf132.png)

       
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
  ![image](https://user-images.githubusercontent.com/111332434/204168722-3c336e73-aa22-4c8d-846e-8975d3616fbb.png)

  
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
![image](https://user-images.githubusercontent.com/111332434/204168735-91f05035-e572-4d24-beeb-bb7d2b64f54a.png)


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
![image](https://user-images.githubusercontent.com/111332434/204168752-5f24469c-51a8-4db8-8302-af7bd61bb67b.png)


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
