class Fp:
    # A class to describe the finite field Fp
    # Example:
    # 
    # (F7, +modp, *modp) = {0,1,2,3,4,5,6}
    # 
    # 

    @classmethod
    def gcd(cls, a, b):
        # Calculates gcd(a,b)

        a,b = abs(a.p),abs(b.p)

        if (b==0):
            return a
        
        return cls.gcd(b, a%b)
        #return gcd(b,a%b)

    def __init__(self, mod, p):
        self.mod = mod
        self.p = p

    def __add__(self, p2):

        return (self.p + p2.p)%self.mod

    def __sub__(self, p2):

        return (self.p-p2.p)%self.mod

    def __mul__(self, p2):

        return (self.p*p2.p)%self.mod
    
    def __mod__(self, p2):

        return (self.p%p2.p)

    def __truediv__(self, p2):
        # Calculates p1/p2 = p1*inv(p2)  (mod p)
        
        # Exception for division by zero:
        if p2.p == 0:
            # Maybe raise?
            return "Division by zero is not defined"

        # check whether inv(p2) exists:
        #if gcd(p2.p, self.mod) != 1:
        #    return "Division is not defined"

    
    # def gcd(self, b):
    #     # Calculates gcd(a,b)

    #     a,b = abs(self.p),abs(b.p)

    #     if (b==0):
    #         return a
        
    #     return Fp.gcd(b,a%b)
    
    
    
    '''


    def inverse(self):
        # Calculates the inverse of self.p using
        # the Extended Euclidean Algorithm
        d,x,y = self.egcd(self.p, self.mod)

        return x


    def egcd(a,b):
        # Calculates gcd recursively

        if(a==0):
            return b,0,1
        
        d,x,y = egcd(b%a,a)

        k1 = y - (b//a) * x
        k2 = x

        return d,k1,k2
    '''


# Driver Code:


p3 = Fp(7,3)
p6 = Fp(7,6)
p0 = Fp(7,0)

# print(f"3+6 = {p3+p6} (mod 7)")    # 3+6 = 9 = 2(mod 7)
# print(f"3-6 = {p3-p6} (mod 7)")    # 3-6 = -3 = 4 (mod 7)
# print(f"3*6 = {p3*p6} (mod 7)")    # 3*6 = 18 = 4 (mod 7)

print(type(p6+p3))
#print(Fp.gcd(p6,p3))