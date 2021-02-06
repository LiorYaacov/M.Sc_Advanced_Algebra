class elliptic_curves:

    def __init__(self,a,b,p):
        
        self.a = a
        self.b = b
        self.p = p

class Point:

    def __init__(self,x,y,p):#,a,b):

        self.x = x
        self.y = y
        #self.a = a
        #self.b = b
        self.p = p

    def __add__(self, p2):

        x1,y1 = self.x,self.y
        x2,y2 = p2.x,p2.y

        # P != Q
        if x1 != x2:
            lambda_ = ((y2-y1)/(x2-x1))
            
            x3 = (( lambda_*lambda_ ) - x1 - x2 ) %self.p
            y3 = (-y1 + (lambda_)*(x1-x3) ) %self.p
        

        #elif p1 == p2:
            
            
            
        #else:
        #    return ('inf','inf')

        return (int(x3),int(y3))


p1 = Point(1,5,11)
p2 = Point(0,1,11)


#print(p1+p2)