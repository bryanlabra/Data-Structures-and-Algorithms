# utils/list_utils.py
import random

def arr(length, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]