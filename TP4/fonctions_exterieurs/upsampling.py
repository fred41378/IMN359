import numpy as np

def upsampling(x, d):
    """
        up-sampling along dimension d by factor p=2
    """
    p = 2
    s = x.shape
    if d == 1:
        y = np.zeros((p * s[0], s[1]))
        y[::p, :] = x
    elif d == 2:
        y = np.zeros((s[0], p * s[1]))
        y[:, ::p] = x
    else:
        raise Exception('Not implemented')
    return y