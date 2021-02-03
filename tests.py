


def eliptic_curve(x1,y1,x2,y2):

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
    



pairs = smooth_curve(43,-1)
print(f"pairs: {pairs}")
print(f"len(pairs) = {len(pairs)}")
'''



# Example 1:
x1,y1 = 0,-1
x2,y2 = 1,1

print(f"(x3,y3) = {eliptic_curve(x1,y1,x2,y2)}")


# Example 2
x1,y1 = -0.577,-1.117
x2,y2 = 0.577,0.784

ec2 = eliptic_curve(x1,y1,x2,y2)
print(f"(x3,y3) = (%.3f,%.3f)" % (ec2[0],ec2[1]))
print(f"y = %.3fx + %.3f" % (ec2[2],ec2[3]))'''