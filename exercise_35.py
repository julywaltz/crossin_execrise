from math import sqrt

class Point(object):
    def __init__(self,x = 0 , y = 0):
        self.x = x
        self.y = y
    def move_to(self,x = 0 ,y = 0):
        self.x = x
        self.y = y
    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s , %s)'%(str(self.x),str(self.y))

p1 = Point(3,5)
p2 = Point(0,1)
print(p1)
print(p2)
print(p1.distance_to(p2))