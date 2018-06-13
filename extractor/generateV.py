import numpy as np

def generateV(source_seq):
    
    l=int((source_seq.shape)[0])
    v=np.zeros(l//2, dtype=int)
    shape_v = 0
    xor = 0

    for i in range(l): 
        xor = (source_seq[2*i]+source_seq[2*i+1]) % 2
        if xor == 0: 
            v[i] = source_seq[2*i]
            shape_v+=1

    v2=np.zeros(shape_v, int)
    
    for i in range(shape_v):
        v2[i]=v[i]

    return v2