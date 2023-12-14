import itertools
import numpy as np

def sequential():
    def matrix(a, b, score=3, cost=2):

        H = np.zeros((len(a) + 1, len(b) + 1), int)

        for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):

            equals = H[i - 1, j - 1] + (score if a[i - 1] == b[j - 1] else - score)
            eliminate = H[i - 1, j] - cost
            insert = H[i, j - 1] - cost
            H[i, j] = max(equals, eliminate, insert, 0)

        return H

    def traceback(H, b, b_='', old_i=0):
        
        flip = np.flip(np.flip(H, 0), 1)
        i_, j_ = np.unravel_index(flip.argmax(), flip.shape)
        i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  
    
        if H[i, j] == 0:
            return b_, j
        
        b_ = b[j - 1] + '-' + b_ if old_i - i > 1 else b[j - 1] + b_

        return traceback(H[0:i, 0:j], b, b_, i)

    def smith_waterman(a, b, score=3, cost=2):

        a, b = a.upper(), b.upper()
        H = matrix(a, b, score, cost)
        b_, pos = traceback(H, b)

        return pos, pos + len(b_)


    print(matrix('GGTTGACTA', 'TGTTACGG'))

    a, b = 'ggttgacta', 'tgttacgg'
    H = matrix(a, b)

    print(traceback(H, b)) # ('gtt-ac', 1)

    a, b = 'GGTTGACTA', 'TGTTACGG'
    start, end = smith_waterman(a, b)

    print(a[start:end])


def parallel():
    def matrix(a, b, score=3, cost=2):

        H = np.zeros((len(a) + 1, len(b) + 1), int)

        for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):

            equals = H[i - 1, j - 1] + (score if a[i - 1] == b[j - 1] else - score)
            eliminate = H[i - 1, j] - cost
            insert = H[i, j - 1] - cost
            H[i, j] = max(equals, eliminate, insert, 0)
            
        return H

    def traceback(H, b, b_='', old_i=0):
        
        flip = np.flip(np.flip(H, 0), 1)
        i_, j_ = np.unravel_index(flip.argmax(), flip.shape)
        i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  
    
        if H[i, j] == 0:
            return b_, j
        
        b_ = b[j - 1] + '-' + b_ if old_i - i > 1 else b[j - 1] + b_

        return traceback(H[0:i, 0:j], b, b_, i)

    def smith_waterman(a, b, score=3, cost=2):

        a, b = a.upper(), b.upper()
        H = matrix(a, b, score, cost)
        b_, pos = traceback(H, b)

        return pos, pos + len(b_)


    print(matrix('GGTTGACTA', 'TGTTACGG'))

    a, b = 'ggttgacta', 'tgttacgg'
    H = matrix(a, b)

    print(traceback(H, b))

    a, b = 'GGTTGACTA', 'TGTTACGG'
    start, end = smith_waterman(a, b)

    print(a[start:end]) 