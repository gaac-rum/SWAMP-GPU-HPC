# main.py
from SmithWaterman_Implementations import sequential as sequential
from SmithWaterman_Implementations import parallel as parallel
import time

#Start Timer
start = time.time()

#Call Sequential Implementation in SmithWaterman_Implementation
sequential()

#End Timer
end = time.time()

#Show time it took to execute sequential implementation
print("Smith-Waterman Algorithm Sequential Implementation execution time:", end - start)

#Start Timer
start = time.time()

#Call Parallel Implementation in SmithWaterman_Implementation
parallel()

#End Timer
end = time.time()

#Show time it took to execute Parallel implementation
print("Smith-Waterman Algorithm Parallel Implementation execution time:", end - start)

