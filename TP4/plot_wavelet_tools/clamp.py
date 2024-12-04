import numpy as np

def clamp(x, a=[], b=[]):
    """
     clamp - clamp a value

       y = clamp(x,a,b);

     Default is [a,b]=[0,1].

       Copyright (c) 2004 Gabriel Peyre
    """

    if a == []:
        a = 0.0
    if b == []:
        b = 1.0
    return np.minimum(np.maximum(x, a), b)
