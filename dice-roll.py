import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import sympy
from math import radians, degrees
from scipy.optimize import minimize
from collections import Counter as count

try:
    import cirq
    from cirq_web import bloch_sphere
    from cirq import Z, PauliSum
except ImportError:
    print("installing cirq...")
    !pip install cirq --quiet
    !pip install cirq-web --quiet
    import cirq
    from cirq_web import bloch_sphere

    print("installed cirq.")


import warnings
warnings.filterwarnings("ignore")


print("Libraries Successfully Imported")





def quantum_random_number():

  #define the random number
  random_number = 0

  while random_number not in  [1, 2, 3, 4, 5, 6]:
    # Step 1: Create qubits
    qubits = cirq.NamedQubit.range(3, prefix = "q")

    # Step 2: Create the quantum circuit
    circuit = cirq.Circuit()

    # Apply Hadamard gates to all qubits to create superposition
    circuit.append(cirq.H.on_each(qubits))

    # Measure all qubits
    circuit.append(cirq.M(qubits, key = "result"))

    # Step 3: Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit)

    # Step 4: Extract the measured bits and convert to integer
    bits = result.measurements["result"][0]
    bitstring = ''.join(str(bit) for bit in bits[::-1])  # MSB first
    random_number = int(bitstring, 2)

  return random_number






#create a list
numbers = []


# Step 6: Roll the die multiple times
#print("Quantum Dice Rolls:")
for i in range(1000):
    numbers.append(quantum_random_number())
#count the number of each output
freq = count(numbers)
freq





# Roll many times to visualize

'''
num_rolls = # Finish Code
rolls = # Finish Code
counts = Counter(rolls)
'''

x = sorted(freq.keys())         # [1, 2, 3, 4, 5, 6]
y = [freq[val] for val in x]    # [161, 165, 153, 176, 167, 178]

# Plot
plt.bar(x, y, color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Quantum RNG results, Simulated')
plt.xticks(x)  # Ensure all values are shown on the x-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.show()