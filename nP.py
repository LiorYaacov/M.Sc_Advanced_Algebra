a, b = -7, 10  # curve coefficients from your exemple


def bits(n):
        while n:
            yield n & 1
            n >>= 1

def add(P, Q):
    if P is None or Q is None: # check for the zero point 
        return P or Q
    xp, yp = P
    xq, yq = Q
    if xp == xq:
        return double(P)
    m = (yp - yq) / (xp - xq)
    xr = m**2 - xp - xq
    yr = yp + m * (xr - xp)
    return (xr, -yr)

def double(P): 
    if P is None:
        return None 
    xp, yp = P 
    m = (3 * xp ** 2 + a) / (2 * yp) 
    xr = m**2 - 2*xp 
    yr = yp + m * (xr - xp) 
    return (xr, -yr)

def double_and_add(n, P):
    result = None # This is our zero point
    addend = P
    for b in bits(n):
        if b:
            result = add(result, addend)
        addend = double(addend)
    return result




print(double_and_add(2, (1,23)))