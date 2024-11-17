import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# utils/algos/mergesort.py
from DataStructuresAndAlgorithms.utils.list_utils import arr, is_sorted # Import arr and is_sorted from utils

def merge(left, right): 
    """Merges two sorted lists into a single sorted list.""" 
    print("\n=== Merging ===")
    print(f"Left half: {left}, Right half: {right}")
    
    sorted_array = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        print(f"Comparing left[{i}] = {left[i]} and right[{j}] = {right[j]}")
        
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            print(f"Appending {left[i]} from left half")
            i += 1
        else:
            sorted_array.append(right[j])
            print(f"Appending {right[j]} from right half")
            j += 1
    
    # Append any remaining elements in either left or right list
    if i < len(left):
        print(f"Extending remaining left half elements: {left[i:]}")
    if j < len(right):
        print(f"Extending remaining right half elements: {right[j:]}")
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    print(f"Merged result: {sorted_array}")
    return sorted_array

def merge_sort(arr):
    print(f"\nDividing: {arr}")
    
    if len(arr) <= 1: 
        return arr  # Return if single-element list, as it's already sorted
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    result = merge(left_half, right_half)
    print(f"Result after merging halves: {result}")
    print("End of this level\n" + "-" * 50)
    return result

def main(): 
    random_array = arr(4, 0, 9)  # Create a random array for testing
    print("Original array:", random_array)

    if not is_sorted(random_array): 
        print("Array is not sorted. Starting merge sort...\n")
        sorted_array = merge_sort(random_array)  
        print("\nFinal sorted array:", sorted_array)
    else:
        sorted_array = random_array
        print("Array is already sorted:", sorted_array)

# Run main() only if this script is executed directly
if __name__ == "__main__":
    main()