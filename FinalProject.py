import time

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
'''

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

def division(x,y,n):
    # Calculates x/y (mod n)  =  x*(inv(y))
    # https://crypto.stanford.edu/pbc/notes/numbertheory/arith.html

    if y%n == 0:
        return "Cannot Divide by Zero"
    
    x,y = x%n,y%n

    # Check if division is defined (i.e. gcd(y,n)=1):
    d,k1,k2 = egcd(y,n)

    if d!=1:
        print("Division is not defined")
        return -1

    while k1<0:
        k1 += n

    return multiply(x,k1,n)

def gcd(a, b):
    # Calculates gcd(a,b)

    a,b = abs(a),abs(b)

    if (b==0):
        return a
    
    return gcd(b,a%b)

def inverse(a,m):
    # Calculate inv(a) mod m

    d,k1,k2 = egcd(a,m)

    while k1<0:
        k1 += m
    
    if d==1:
        return k1

def inverse_fermat(a,m):
    # Calculates inv(a) using Fermat's Theorem:
    # inv(a) = a^(p-2)
    # https://crypto.stanford.edu/pbc/notes/numbertheory/order.html

    return pow(a,m-2)%m

def egcd(a,b):
    # Calculates gcd recursively

    if(a==0):
        return b,0,1
    
    d,x,y = egcd(b%a,a)

    k1 = y - (b//a) * x
    k2 = x

    return d,k1,k2


def exp_by_square(base, exp, m):
    # Calculates base^exp using squaring

    if (exp == 0):
        return 1
    if (exp == 1):
        return base%m
    
    x = exp_by_square(base, exp//2, m)
    x = (x*x) % m

    if (exp%2 == 0):
        return x
    else:
        return (((base%m) * x) % m)
    
def safe_prime_mul_order(p,m):

    if (p**1)%m == 1:
        return 1
    elif (p**2)%m == 1:
        return 2
    elif (exp_by_square(p,((m-1)/2),m)) == 1:
        return int((m-1)/2)
    elif (exp_by_square(p,m-1,m)) == 1:
        return m-1

# Driver Code:

start_time = time.time()
print(exp_by_square(83,10001,1501))
end_time = time.time()
print(end_time-start_time)

