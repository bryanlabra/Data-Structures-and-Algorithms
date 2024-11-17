import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))# Add the root project directory to PYTHONPATH

 # utils/algos/mergesort.py
from utils import arr, is_sorted  # Import arr and is_sorted from utils

def merge(left, right):
    """Merges two sorted arrays into a single sorted array."""
    sorted_array = []
    i = j = 0

    # Compare elements from both halves and add the smaller one to the sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add any remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

def merge_sort(arr):
    """Sorts the array using merge sort and returns the sorted array."""
    if len(arr) <= 1:
        return arr
 