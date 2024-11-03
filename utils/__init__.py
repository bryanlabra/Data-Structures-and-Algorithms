# utils/__init__.py
from .list_utils import arr            # Import arr from list_utils
from .algos import *

__all__ = [
    "arr",           # Expose arr function
    "binary_search", # Expose binary_search function
    "mergesort"      # Expose mergesort module
]