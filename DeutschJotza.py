import numpy as np
from qiskit import QuantumCircuit, transpile
import matplotlib.pyplot as plt
from qiskit import Aer
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram

simulator = Aer.get_backend('qasm_simulator')
print("+---------------Función 1------------------+")
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
#circuit.cnot(1,4)
#circuit.cnot(2,4)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.barrier()
circuit.measure([0,1,2,3], [0,1,2,3])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
print("+---------------Función 2------------------+")
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
#circuit.cnot(1,4)
#circuit.cnot(2,4)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.barrier()
circuit.measure([0,1,2,3], [0,1,2,3])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
print("+---------------Función 3------------------+")
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
#circuit.cnot(1,4)
#circuit.cnot(2,4)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.barrier()
circuit.measure([0,1,2,3], [0,1,2,3])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
print("+---------------Función 4------------------+")
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
#circuit.cnot(0,4)
#circuit.cnot(1,4)
#circuit.cnot(2,4)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.barrier()
circuit.measure([0,1,2,3], [0,1,2,3])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
