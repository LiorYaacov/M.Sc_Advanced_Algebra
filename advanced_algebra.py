import time
import math
import numpy as np
from matplotlib import pyplot as plt

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
        
        if exp == 0:
            return 1

        for _ in range(2,exp+1):
            base *= self.p
            base %= self.mod
        
        return base
            


    def inverse(self):
        # Calculates the inverse of self.p using
        # the Extended Euclidean Algorithm
        #
        # Apply to multiplication only

        # Get d,x,y (where: x*mod + y*p = d)

        d,x,y = Fp.egcd(self.mod, self.p)

        while(y<0):
            y += self.mod
        return y


    def group_orders(self):                                                     # Might be unused
        # Returns group's orders in a tuple
        # 
        # (add_group_order, mul_group_order)

        add_group_order = self.mod
        mul_group_order = self.mod-1
        
        return (add_group_order,mul_group_order)

    def add_element_order(self):
        # Calculates the order of p (+ mod p)
        
        i=1
        current = self.p
        
        while(current != self.e_add):
            current += 1
            current %= self.mod
            i += 1
        
        return i


    def mul_element_order(self):
        # Calculates the order of p (* mod p)
        
        i=1
        current = self.p
        
        while(current != self.e_mul):
            current *= self.p
            current %= self.mod
            i += 1
        
        return i
    


    def exp_by_square(self, base, exp, m):
    # Calculates base^exp%m using squaring

        if (exp == 0):
            return 1
        if (exp == 1):
            return base%m
        
        x = self.exp_by_square(base, exp//2, m)

        print(f"{base}^{exp} = {x}")
        
        x = (x*x) % m

        
        if (exp%2 == 0):
            return x
        else:
            return (((base%m) * x) % m)


class EllipticCurves:

    def __init__(self,a,b,p):
        
        self.a = a
        self.b = b
        self.p = p
    

    def affine_elliptic_curve_points(self):
        
        points = []

        for x in range(self.p):
            for y in range(self.p):
                # if z=0 -> infinity point
                if x==y==0:
                    continue
                
                # y^2 - x^3 - a*x - b = 0
                c1 = (y**2)%self.p
                c2 = (x**3)%self.p
                c3 = (self.a*x)%self.p
                c4 = self.b%self.p

                C = (c1-c2-c3-c4)%self.p

                if C == 0:
                    points.append( (x,y) )

        return points
    
    def Hasses_bound(self):
        
        lower_bound = int(self.p + 1 - (2*math.sqrt(self.p)))
        upper_bound = int(self.p + 1 + (2*math.sqrt(self.p)))

        print(f"{lower_bound} <= #C(Fp) <= {upper_bound}")

    def show_points(self):

        points = self.affine_elliptic_curve_points()

        for i in points:
            plt.scatter(i[0],i[1],  color='black')
        plt.grid()
        plt.title(f"a={self.a}, b={self.b}, Number of Points: {len(points)} (w/o infinity)")
        plt.show()

        return points

class Point(Fp):

    @classmethod
    def is_on_curve(cls,x,y,p,a,b):
        # Checks if the point is on the curve (defined by a and b)

        return (((y**2 - x**3 - (a*x) - b))%p == 0)
        #return (((self.y**2 - self.x**3 - (self.a*self.x) - self.b))%self.p == 0)

    def __repr__(self):

        return f"({self.x},{self.y})"

    def __init__(self,x,y,p,a,b):
        
        if x==y==0:
            print("Point at infinity")

        if not Point.is_on_curve(x,y,p,a,b):
            print(f"Please notice: {(x,y)} is not on the curve")

        self.x = x
        self.y = y
        self.p = p
        self.a = a
        self.b = b
        self.order = None


    def __add__(self, p2):
        
        ## TBD
        # Add P + (-P) = 0
        # Add P + 0 = 0 + P = P

        x1,y1 = self.x,self.y
        x2,y2 = p2.x,p2.y


        # Handle P+0 and 0+P:
        if x1==y1==0:
            return p2
        elif x2==y2==0:
            return self

        # Check if Q is on the curve defined by P's parameters
        if not Point.is_on_curve(x2,y2,self.p,self.a,self.b):
            return f"{self} and {p2} are not on the same curve"

        
        
        # P != Q
        if x1 != x2:
            lambda_ = (y2-y1) * (Fp.inverse(Fp(x2-x1,self.p)))
            
            x3 = (( lambda_**2 ) - x1 - x2 ) %self.p
            y3 = (-y1 + (lambda_)*(x1-x3) ) %self.p

            return Point(int(x3),int(y3),self.p,self.a,self.b)
        

        elif x1==x2 and y1==y2:
            
            h1 = (3*(x1**2) + self.a)
            h2 = Fp.inverse(Fp(2*y1, self.p))
            
            lambda_ = (h1 * h2) % self.p
            #lambda_ = (3*(x1**2) + self.a) * (Fp.inverse(Fp(2*y1,self.p)))

            x3 = (  (lambda_**2) - (2*x1)  ) % self.p
            y3 = ( -y1 + (lambda_*(x1-x3)) ) % self.p

            return Point(int(x3),int(y3),self.p,self.a,self.b)
            
            
        else:
            return (0,0)

    
    def inverse(self):
        # Returns -P

        y_inv = -self.y

        while(y_inv<0):
            y_inv += self.p

        return (self.x, y_inv)

    def generate(self, calc_order=0):
        # Generates the elements of <P>
        # if calc_order==1: calculates the order of P

        if not calc_order:
            print(f"<{self}> = {self}", end="") 
        
        P_temp = self
        order = 1

        while (P_temp != (0,0)):
            P_temp += self
            order += 1
            if calc_order:                              # Only calculate order (without printing <P> elements)
                continue
            print(f",{P_temp}", end="")
        
        return order    

        # Verification:
        # https://graui.de/code/elliptic2/
        

    def point_order(self):
        
        return self.generate(calc_order=1)
        # http://www.christelbach.com/ECCalculator.aspx


    def bits(self, n):
        while n:
            yield n & 1
            n >>= 1

    def double_and_add(self, n):
        
        # TBD
        # if P = (0,0) return infinity

        result = Point(0,0,self.p,self.a,self.b)
        accumulator = self
        

        for i in self.bits(n):
            if i:
                result += accumulator
            accumulator += accumulator
        return result

    def nP(self, n):

        # How To:
        # https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/

        # Verify results using:
        # http://www.christelbach.com/ECCalculator.aspx
        
        
        pass




# --------------------------------- #
# Hasse's Theorem

# C = EllipticCurves(1,1,11)
#print(C.affine_elliptic_curve_points())
#C.Hasses_bound()

# C.show_points()


# --------------------------------- #

# --------------------------------- #
# nP Calculation #

# p = Point(3,104,263,5,-9)

# print(p.double_and_add(89))
#print(p.nP(2))
# --------------------------------- #



#################
# Driver

# EllipticCurve
        # ec = EllipticCurves(1,1,263)
        # print(ec.affine_elliptic_curve_points())



# --------------------------------- #
# Points Addition
# P = Point(2,167,263,1,1)
# Q = Point(2,96,263,1,1)

# print(P+Q)


# Adding points that are not on the same curve:
# P = Point(2,167,263,1,1)
# Q = Point(2,96,263,1,1)

# print(P+Q)


# Creating the point at infinity
# Should raise a ValueError
#
# P = Point(0,0,263,1,1)
# print(P+P)
# --------------------------------- #



# --------------------------------- #
# Point Inverse
# p1 = Point(6,152,263)
# print(p1.inverse())
# --------------------------------- #




# --------------------------------- #
# Point Generator <P>
# P = Point(8,235,263,1,1)

# P.generate()
# --------------------------------- #


# --------------------------------- #
# is_on_curve

#P = Point(1,22,263,1,1)
# --------------------------------- #



# --------------------------------- #
# Point Order

# P = Point(1,23,263,1,1)
# Q = Point(8,235,263,1,1)

# P.point_order()         # 130
# Q.point_order()         # 65
# --------------------------------- #