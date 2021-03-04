import time
import math
import random
import numpy as np
from mpldatacursor import datacursor
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
            return "Division by zero is not defined"

        # check whether inv(p2) exists:
        if Fp.gcd(p2.mod, p2.p) != 1:
            return "Division is not defined"
        
        # Calculate inv(p2)
        p2_inv = Fp(Fp.inverse(p2), self.mod)

        return (self.p * p2_inv.p)%self.mod
    
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
            if current==0:
                return None
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
        x = (x*x) % m
        
        if (exp%2 == 0):
            return x
        else:
            return (((base%m) * x) % m)

    def safe_prime_mul_order(self):

        if (self.p)%self.mod == 1:
            return 1
        elif (self.p**2)%self.mod == 1:
            return 2
        elif (self.exp_by_square(self.p,((self.mod-1)/2),self.mod)) == 1:
            return int((self.mod-1)/2)
        elif (self.exp_by_square(self.p,self.mod-1,self.mod)) == 1:
            return self.mod-1

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
    
    def smooth_curve(self,k):

        # Returns k pairs of (a,b) that satisfied: 4a^3 + 27b^2 != 0
        # (if exist)
        #
        # use k == -1 to calculate all pairs exist

        pairs = []
        for a in range(2,self.p):
            for b in range(2,self.p):
                result = (4*(a**3) + 27*(b**2))%self.p
                if result != 0:
                    pairs.append((a,b))
                    k -= 1
                    print(f"4*{a}^3 + 27*{b}^2 = {result} (mod {self.p})")

                    if k == 0:
                        return pairs
        
        return pairs

    def Hasses_bound(self):
        
        lower_bound = int(self.p + 1 - (2*math.sqrt(self.p)))
        upper_bound = int(self.p + 1 + (2*math.sqrt(self.p)))

        print(f"{lower_bound} <= #C(Fp) <= {upper_bound}")

    def show_points(self):
        fig, ax = plt.subplots()
        ax.set_title('Click on a dot to display its label')

        # # Plot a number of random dots
        # for i in range(1, 1000):
        #     ax.scatter([random.random()], [random.random()], label='$ID: {}$'.format(i))

        points = self.affine_elliptic_curve_points()

        for i in points:
            ax.scatter(i[0],i[1], color='red', label='$ID: {}$'.format(i), edgecolor="black", s=8)

        # Use a DataCursor to interactively display the label for a selected line...
        datacursor(formatter='{label}'.format,bbox=dict(fc='green'), draggable=True)

        plt.grid()
        plt.title(f"a={self.a}, b={self.b}, Number of Points: {len(points)} (w/o infinity)")
        plt.show()
    
    def plot_curve(self):

        # Plot curve
        y, x = np.ogrid[-5:5:100j, -5:5:100j]

        curve = (y**2) - (x**3) - (self.a*x) - self.b
        plt.contour(x.ravel(), y.ravel(), curve, [0])
        plt.grid()
        plt.title(f"a={self.a}, b={self.b}")
        
        # Plot axis
        plt.axvline(x=0, color='k')
        plt.axhline(y=0, color='k')

        #datacursor(formatter='{label}'.format,bbox=dict(fc='green'), draggable=True)

        plt.show()

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
        
        P_temp = self
        P_elements = []
        order = 1

        while (P_temp != (0,0)):
            P_temp += self
            order += 1
            if calc_order:                              # Only calculate order (without printing <P> elements)
                continue
            #print(f",{P_temp}", end="")
            P_elements.append(P_temp)
        
        if calc_order:
            return order
        return P_elements

        # Verification:
        # https://graui.de/code/elliptic2/
    def point_order(self):
        
        return self.generate(calc_order=1)
        # http://www.christelbach.com/ECCalculator.aspx
    def bits(self, n):
        #
        # Converting n to it's binary representation

        while n:
            yield n & 1
            n >>= 1
    def double_and_add(self, n):
        #
        # Calculates n*P using the Double and Add algorithm

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

        result = self.double_and_add(n)
        return result



