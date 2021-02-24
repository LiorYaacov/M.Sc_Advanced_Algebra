import math
import numpy as np
import matplotlib.pyplot as plt


def eliptic_curve(x1,y1,x2,y2):
    
    # Might Be Unused
    x3 = ( (y2-y1)/(x2-x1) )**2 - x1 - x2
    y3 = -y1 + ( (y2-y1)/(x2-x1) )*(x1-x3)

    m = ( (y2-y1)/(x2-x1) )
    b = y1 - m*x1

    return x3,y3,m,b


def CFp():
    pass

def smooth_curve(p,k):

    # Returns k pairs of (a,b) that satisfied: 4a^3 + 27b^2 != 0
    # (if exist)
    #
    # use k == -1 to calculate all pairs exist

    pairs = []
    for a in range(2,p):
        for b in range(2,p):
            result = (4*(a**3) + 27*(b**2))%p
            if result != 0:
                pairs.append((a,b))
                k -= 1
                print(f"4*{a}^3 + 27*{b}^2 = {result} (mod {p})")

                if k == 0:
                    return pairs
    
    return pairs
    

def affine_elliptic_curve_points(a,b,p):
    points = []
    related = [(0,0)]

    for x in range(p):
        for y in range(p):
            # if z=0 -> infinity point
            if x==y==0:
                continue
            
            # y^2 - x^3 - a*x - b = 0
            c1 = (y**2)%p
            c2 = (x**3)%p
            c3 = (a*x)%p
            c4 = b%p

            C = (c1-c2-c3-c4)%p

            if C == 0:
                points.append( (x,y) )

    return points
    
def add_points(p1,p2,p):
    # Returns the results of p1+p2 (mod p)
    
    x1,y1 = p1
    x2,y2 = p2

    # P != Q
    if x1 != x2:
        lambda_ = ((y2-y1)/(x2-x1))
        
        x3 = (( lambda_*lambda_ ) - x1 - x2 ) %p
        y3 = (-y1 + (lambda_)*(x1-x3) ) %p
    

    elif p1 == p2:
        pass
        
        
    else:
        return ('inf','inf')

    return (int(x3),int(y3))


def plot_curve(a,b,p):

    # Plot curve
    y, x = np.ogrid[-5:5:100j, -5:5:100j]

    curve = (y**2) - (x**3) - (a*x) - b
    plt.contour(x.ravel(), y.ravel(), curve, [0])
    plt.grid()
    
    # Plot axis
    plt.axvline(x=0, color='k')
    plt.axhline(y=0, color='k')

    # X and Y limits
    # plt.xlim(-10,10)
    # plt.ylim(-10,10)

    # Plot point on graph
    #plt.scatter([0],[1])


    plt.show()


def projective_elliptic_curve_points(a,b,p):

    points = []
    related = [(0,0,0)]

    for x in range(p):
        for y in range(p):
            for z in range(p):
                # if z=0 -> infinity point
                if x==y==z==0:
                    continue
                
                # Y^2*Z - X^3 - a*X*Z^2 - b*Z^3 = 0
                c1 = ((y**2)*z)%p
                c2 = (x**3)%p
                c3 = (a*x*(z**2))%p
                c4 = (b*(z**3))%p

                C = (c1-c2-c3-c4)%p

                if C == 0:

                    if (x,y,z) not in related:
                        points.append( (x,y,z) )
                        print(f"{x}:{y}:{z}")
                    
                        # Find all related points
                        (x1,y1,z1) = (x,y,z)

                        while not ((x1,y1,z1) == (0,0,0)):
                            (x1,y1,z1) = ((x1+x)%p,(y1+y)%p,(z1+z)%p)
                            if (x1,y1,z1) not in related:
                                related.append((x1,y1,z1))

    return points

a,b,p = 3,-5,211

''' Projective Elliptic Curve '''
ppoints = projective_elliptic_curve_points(a,b,p)
print(ppoints)
# print(len(ppoints))

''' Affine Elliptic Curve '''
# points = affine_elliptic_curve_points(a,b,p)
# print(points)


''' Add Points '''
# print(add_points((1,5),(0,1),11))
# print(add_points((1,6),(2,0),11))
# print(add_points((2,0),(2,0),11))


plot_curve(-3,5,5)

# Switching to windows