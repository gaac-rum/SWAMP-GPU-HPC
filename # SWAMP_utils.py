# SWAMP_utils.py
import numpy as np

def generate_data(size):
    return np.random.rand(size).astype(np.float32)

def print_result(result):
    print("Result:", result)
