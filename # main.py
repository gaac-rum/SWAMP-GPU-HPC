# main.py
from SWAMP_algorithm import swamp_algorithm
from utils.SWAMP_utils import generate_data, print_result

# Example usage
size = 1000
a = generate_data(size)
b = generate_data(size)

result = swamp_algorithm(a, b)
print_result(result)
