import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
simulator = Aer.get_backend('qasm_simulator')
print("+---------------Función 1------------------+")
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

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
print("+---------------Función 2------------------+")
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

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()

print("+---------------Función 3------------------+")
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

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()
print("+---------------Función 4------------------+")
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

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()