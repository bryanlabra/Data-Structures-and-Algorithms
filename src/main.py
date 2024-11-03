# src/main.py

import sys
import os

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

import random as rand
from DataStructuresAndAlgorithms.utils import arr  # Import arr from utils
from DataStructuresAndAlgorithms.utils.algos import binary_search  # Import binary_search from algos

def main():
    # Generate a random array
    random_array = arr(10, 1, 50)
    print("Original array:", random_array)

    # Sort the array for binary search
    sorted_array = sorted(random_array)
    print("Sorted array:", sorted_array)

    # Choose a random target to search for
    target = rand.choice(sorted_array)
    print("Target to find:", target)

    # Perform binary search
    index = binary_search(sorted_array, target)

    # Output the result
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in the array.")

if __name__ == "__main__":
    main()