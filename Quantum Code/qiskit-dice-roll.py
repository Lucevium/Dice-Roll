# INSTALL LIBRARIES
%pip install qiskit-aer==0.12.0
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import sympy
from math import radians, degrees
from scipy.optimize import minimize
from collections import Counter as count


try:
    import qiskit as qk
except ImportError:
    print("installing qiskit...")
    !pip install cirq --quiet
    !pip install cirq-web --quiet

    print("installed qiskit.")

import warnings
warnings.filterwarnings("ignore")



#CIRCUIT
from math import log2, ceil
def quantum_random_number(sides=6):

  #define the random number
  random_number = 0

  # Number of qubits needed to represent the range

  num_qubits = ceil(log2(sides))

  max_range = 2 ** num_qubits

  while random_number not in  [1, 2, 3, 4, 5, 6]:

    # Step 2: Create the quantum circuit
    circuit = qk.QuantumCircuit(3,3)

    # Apply Hadamard gates to all qubits to create superposition
    circuit.h(range(3))

    # Measure all qubits
    circuit.measure(range(3), range(3))

    # Step 3: Simulate the circuit
    simulator = qk.Aer.get_backend('qasm_simulator')
    job = qk.execute(circuit, simulator, shots=1)
    result = j#create a list
numbers = []


# Step 6: Roll the die multiple times
#print("Quantum Dice Rolls:")
for i in range(1000):
    numbers.append(quantum_random_number())
#count the number of each output
freq = count(numbers)
freq
ob.result()

    # Step 4: Extract the measured bits and convert to integer
    counts = result.get_counts(circuit)
    bitstring = list(counts.keys())[0]
    random_number = int(bitstring, 2)

  return random_number


