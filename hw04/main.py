class Shapes():
    def q(self):
        self.area

    def P(self):
        self.p()
        return self.area
            
class Square(Shapes):
    def __init__(self,a):
        self.a = a

    def p(self):
        self.area = self.a * self.a 
        print(self.area)
        return self.area
    
    
class Circle(Shapes):
    def __init__(self,r):
        self.r = r

    def p(self):
        self.area = self.r * 3.14 * self.r
        print(self.area)
        return float(self.area)

class Ellipse(Shapes):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def p(self):
        self.area =self.a * 3.14 *self.b 
        print(self.area)
        return self.area
    
class Rectange(Shapes):
    def __init__(self,h,w):
        self.h = h
        self.w = w

    def p(self):
        self.area = self.h * self.w
        print(self.area)
        return self.area
    


shapes = [Ellipse(10,20),Square(15),Circle(5),Rectange(20,15),Circle(5),Square(15),Ellipse(10,20)]

def computer_area(shapes):
    s = 0
    for i in range(0,len(shapes)):
        s = s + shapes[i].P()
    return s

total_area = computer_area(shapes)
print(total_area)


        
        
        
       
        

    




    
