import numpy as np

def subsampling(x, d):
    # subsampling along dimension d by factor p=2
    p = 2
    if d == 1:
        y = x[::p, :]
    elif d == 2:
        y = x[:, ::p]
    else:
        raise Exception('Not implemented')
    return y