# DataStructuresAndAlgorithms/utils/__init__.py
from .list_utils import arr, is_sorted
from .algos.mergesort import merge_sort  # Optional if you want merge_sort to be accessible directly from utils
from .algos.binarysearch import binary_search

# If you also need binary_search, you could add it here similarly

__all__ = ["arr", "is_sorted", "merge_sort", "binary_search"]  # Define what is exposed in `utils`