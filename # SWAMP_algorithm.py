# SWAMP_algorithm.py
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda import gpuarray
from kernels.SWAMP_kernel import swamp_kernel

def swamp_algorithm(a, b):
    size = len(a)

    # Allocate GPU memory
    a_gpu = gpuarray.to_gpu(a)
    b_gpu = gpuarray.to_gpu(b)
    result_gpu = gpuarray.empty_like(a_gpu)

    # Define grid and block dimensions
    block_size = 256
    grid_size = (size + block_size - 1) // block_size

    # Launch the GPU kernel
    swamp_kernel(a_gpu, b_gpu, result_gpu, np.int32(size), block=(block_size, 1, 1), grid=(grid_size, 1))

    # Copy result back to host
    result = result_gpu.get()

    return result
