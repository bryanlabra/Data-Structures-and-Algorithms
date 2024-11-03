# Requires array to first be sorted
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils import arr  # Corrected import for the renamed function
import random as rand

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

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

# Run main() only if this script is executed directly
if __name__ == "__main__":
    main()