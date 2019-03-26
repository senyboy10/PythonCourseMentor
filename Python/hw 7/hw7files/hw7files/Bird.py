import math
from Pig import *

class Bird(object):
    def __init__(self, n, x0, y0, r0, dx0, dy0): #initializes class Bird
        self.name = n
        self.x = float(x0)
        self.y = float(y0)
        self.r = float(r0)
        self.dx = float(dx0)
        self.dy = float(dy0)
        
    def move(self): #moves the bird by a distance dx and dy
        self.x += self.dx
        self.y += self.dy
        
    def check_intersect(self, pig): #checks if a bird intersects and hits a pig, passed as a parameter
        dist_x = self.x - float(pig.x)
        dist_y = self.y - float(pig.y)
        return math.sqrt(dist_x**2 + dist_y**2) <= (float(pig.radius) + self.r)
    
    def check_boundary(self): #checks if a bird is no longer within the boundaries
        return self.x + self.r > 1000 or self.y + self.r > 1000 or self.x - self.r < 0 or self.y - self.r < 0
    
    def change_speed(self): #reduces the speed by 50%
        self.dx = self.dx * 0.5
        
    def min_speed(self): #checks if the speed has fallen below 6
        return math.sqrt(self.dx**2 + self.dy**2) <= 6
    
    