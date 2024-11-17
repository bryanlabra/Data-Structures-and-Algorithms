#binary search complexity == O(log n)

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# DataStructuresAndAlgorithms/utils/algos/binarysearch.py
import random as rand
from DataStructuresAndAlgorithms.utils import arr, is_sorted, merge_sort

def binary_search(arr, target):
    # Check if array is sorted
    if not is_sorted(arr):
        print("Array is not sorted. Sorting array before binary search...")
        sorted_array = merge_sort(arr)
        print("Sorted array:", sorted_array)
    
    # Binary search logic here
    left, right = 0, len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    # Generate a random array
    random_array = arr(10, 1, 50)
    print("Original array:", random_array)

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