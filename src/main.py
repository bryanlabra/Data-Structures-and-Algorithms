# src/main.py
import sys
import os
import random as rand

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(project_root)

from DataStructuresAndAlgorithms.utils import arr, is_sorted, merge_sort, binary_search

def main():
    # Generate a random array
    random_array = arr(10, 1, 50)
    print("Original array:", random_array)

    # Check if the array is sorted, if not, perform merge sort
    if not is_sorted(random_array):
        print("Array is not sorted. Sorting array...")
        sorted_array = merge_sort(random_array)  # Sort the array if not sorted
        print("Sorted array:", sorted_array)
    else:
        sorted_array = random_array
        print("Array is already sorted:", sorted_array)
    
    # Choose a random target to search for
    target = rand.choice(random_array)
    print("Target to find:", target)

    # Perform binary search
    index = binary_search(random_array, target)

    # Output the result
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in the array.")

# Run main() only if this script is executed directly
if __name__ == "__main__":
    print("\n")
    main()
    print("\n")
