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

        if abs(a) < abs(b):
            return cls.gcd(b,a)

        if (b==0):
            return a
        
        return cls.gcd(b, a%b)

    @classmethod
    def egcd(cls, a, b):
        # Calculates the extended gcd (recursively)

        if(a==0):
            return b,0,1
        
        d,x,y = cls.egcd(b%a,a)

        k1 = y - (b//a) * x
        k2 = x

        return d,k1,k2    





    def __init__(self, p, mod):
        self.p = p%mod
        self.mod = mod
        self.e_add = 0
        self.e_mul = 1

    def __add__(self, p2):
        if isinstance(p2, Fp):
            return (self.p + p2.p)%self.mod
        else:
            return (self.p+p2)%self.mod

    def __sub__(self, p2):

        return (self.p-p2.p)%self.mod

    def __mul__(self, p2):
        
        if isinstance(p2, Fp):
            return (self.p*p2.p)%self.mod
        
        else:
            return (self.p*p2)%self.mod
    
    def __mod__(self, p2):

        return Fp(self.mod, self.p%p2.p)

    def __truediv__(self, p2):
        # Calculates p1/p2 = p1*inv(p2)  (mod p)
        
        # Exception for division by zero:
        if p2.p == 0:
            # Maybe raise?
            return "Division by zero is not defined"

        # check whether inv(p2) exists:
        if Fp.gcd(p2.mod, p2.p) != 1:
            return "Division is not defined"
        
        # Calculate inv(p2)
        p2_inv = Fp(Fp.inverse(p2), self.mod)

        return (self.p * p2_inv.p)%self.mod
    
    # def __pow__(self, p2):

    #     if isinstance(p2, Fp):
    #         return (self.p**p2.p)%self.mod
    #     else:
    #         return (self.p**p2)%self.mod
    
    def __pow__(self, p2):

        base = self.p

        if isinstance(p2, Fp):
            exp = p2.p
        else:
            exp = p2
        
        for _ in range(2,exp+1):
            base *= self.p
            base %= self.mod
        
        return base
            


    def inverse(self):
        # Calculates the inverse of self.p using
        # the Extended Euclidean Algorithm
        d,x,y = Fp.egcd(self.mod, self.p)

        return y


    def add_element_order(self):
        # Calculates the order of p (+ mod p)
        
        i=1
        order = self.p
        
        while(order != self.e_add):
            order = self+order
            i += 1
        
        return i


    def mul_element_order(self):
        # Calculates the order of p (* mod p)
        
        i=1
        order = self.p
        
        while(order != self.e_mul):
            order = self*order
            i += 1
        
        return i

    def safe_prime_order(self):
        pass
        # TBD
        # if self**1 == 1:
        #     return 1
        # elif self**2 == 1:
        #     return 2
        # elif self**(self.mod - 1) == 1:
        #     return self.mod - 1
        # elif self**((self.mod-1)/2) == 1:
        #     return (self.mod-1)/2

'''
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

p0 = Fp(0,7)
p1 = Fp(1,7)
p2 = Fp(2,7)
p3 = Fp(3,7)
p4 = Fp(4,7)
p5 = Fp(5,7)
p6 = Fp(6,7)


# print(f"3+6 = {p3+p6} (mod 7)")    # 3+6 = 9 = 2(mod 7)
# print(f"3-6 = {p3-p6} (mod 7)")    # 3-6 = -3 = 4 (mod 7)
# print(f"3*6 = {p3*p6} (mod 7)")    # 3*6 = 18 = 4 (mod 7)


#print(Fp.gcd(Fp(21,7),Fp(3,7)))
'''
print(f"5/2 = {p5/p2} (mod 7)")     # 5/2 = 6 (mod 7)
print(f"5/3 = {p5/p3} (mod 7)")     # 5/3 = 4 (mod 7)

print("Multiplication Orders:")
print("---------------------")
print(f"o(1) = {p1.mul_element_order()}")
print(f"o(2) = {p2.mul_element_order()}")
print(f"o(3) = {p3.mul_element_order()}")
print(f"o(4) = {p4.mul_element_order()}")


print("Addition Orders:")
print("---------------------")
print(f"o(0) = {p0.add_element_order()}")
print(f"o(1) = {p1.add_element_order()}")
print(f"o(2) = {p2.add_element_order()}")



'''
p2_23 = Fp(2,23)
p20_23 = Fp(20,23)
print(f"o(2) (mod23) = {p2_23.mul_element_order()}")
print(f"o(20) (mod23) = {p20_23.mul_element_order()}")


p2_263 = Fp(2,263)
p9_263 = Fp(9,263)
p255_263 = Fp(255,263)
p256_263 = Fp(256,263)

'''
#print(p3.safe_prime_order())
print(f"o(2) (mod 263) = {p2_263.safe_prime_order()}")
print(f"o(9) (mod 263) = {p9_263.safe_prime_order()}")
print(f"o(255) (mod 263) = {p255_263.safe_prime_order()}")
print(f"o(256) (mod 263) = {p256_263.safe_prime_order()}")


print(f"** o(2) (mod 263) = {p2_263.mul_element_order()}")

'''
print(f"2^131 (mod 263) = {p2_263**131}")
print(f"2^255 (mod 263) = {p2_263**255}")

print(f"o(2) (mod 263) = {p2_263.safe_prime_order()}")

#print("power - exponent")
#print(p4**3)
# for i in range(2,7):
#     print(p4**i)