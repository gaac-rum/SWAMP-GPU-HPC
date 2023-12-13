# SWAMP_kernel.cu
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda import gpuarray
from pycuda.compiler import SourceModule

mod = SourceModule("""
    __global__ void swamp_kernel(float *a, float *b, float *result, int size) {
        int idx = threadIdx.x + blockDim.x * blockIdx.x;
        if (idx < size) {
            result[idx] = a[idx] + b[idx];
        }
    }
""")

swamp_kernel = mod.get_function("swamp_kernel")
