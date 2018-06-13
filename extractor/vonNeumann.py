import math
import numpy as np

def vonNeumann(source_seq):
    l=int((source_seq.shape)[0])
    b=np.zeros(l//2, dtype=int)
    shape_b=0

    for i in range(l//2)):
        xor = (source_seq[2*i]+source_seq[2*i+1]) % 2
        if xor == 1: 
            b[i] = source_seq[2*i]
            shape_b+=1
    b2=np.zeros(shape_b, dtype=int)
    for i in range(shape_b):
        b2[i]=b[i]

    return b2