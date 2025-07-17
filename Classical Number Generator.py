import random
import matplotlib.pyplot as plt
from collections import Counter

def classical_quantum_number_generator(upper_bound):
  """
  Simulates a "classical quantum number generator" using a random number.

  Args:
    upper_bound: The upper limit (exclusive) for the generated number.

  Returns:
    A random integer between 0 (inclusive) and upper_bound (exclusive).
  """
  return random.randint(0, upper_bound - 1)

# Example usage:
generated_number = classical_quantum_number_generator(10)
print(f"Generated classical 'quantum' number: {generated_number}")
def roll_die():
  # Simulate a die roll (classical PRNG)
  return classical_quantum_number_generator(6) + 1 # Assuming 1-6 roll

print ("Classical 'quantum' generator:")
numbers = [] # Initialize an empty list to store numbers
for i in range (1000):
      numbers.append(roll_die()) # Call the roll_die function to get a number

freq = Counter(numbers) # Use Counter to count frequencies

x = sorted(freq.keys())   #[1,2,3,4,5,6]
y= [freq[val] for val in x]     #[frequency for each value] # Corrected list comprehension

plt.bar(x,y, color= 'purple', edgecolor = 'black') # Corrected bar function call
plt.xlabel('value')
plt.ylabel('Frequency')
plt.title('Classical PRNG results, Simulated')
plt.xticks(x) #Ensure all values are shown on the x-axis
plt.grid(axis='y', linestyle='--')
plt.show()

# The second plt.show() is redundant and can be removed
