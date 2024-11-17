# utils/list_utils.py
import random

def arr(length, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]

def is_sorted(arr):
    """Check if the array is sorted in non-decreasing order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))