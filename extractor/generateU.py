import numpy as np

def generateU(source_seq):

    l=int((source_seq.shape)[0])
    u=np.zeros(l//2, dtype=int)    
    shape_u = int((u.shape)[0])

    for i in range(shape_u):
        u[i]=(a[2*i]+a[2*i+1])%2
            
    return u