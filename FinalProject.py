'''
Fp = (Zp, +mod p, *mod p)

Example:
    F7 = {0,1,2,3,4,5,6}

    p1 = 3
    p2 = 5

    p1+p2 = 8(mod 7) = 1
    p1-p2 = -2(mod 7) = 5
    p1*p2 = 15(mod 7) = 1
    p1/p2 = 


def addition(p1,p2,m):

    sum = p1+p2
    
    while sum<0:
        sum += m
    
    return sum%m

def subtract(p1,p2,m):

    diff = p1-p2

    while diff<0:
        diff += m
    
    return diff%m

def multiply(p1,p2,m):

    product = p1*p2

    while product<0:
        product += m
    
    return product%m

def division(p1,p2,m):

    # TBD


def rgcd(a,b):
    # Calculates gcd recursively

    if(a==0):
        return b,0,1
    
    d,x,y = rgcd(b%a,a)

    k1 = y - (b//a) * x
    k2 = x

    return d,k1,k2