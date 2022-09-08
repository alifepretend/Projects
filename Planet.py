import math

class World:
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
        

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
    
    def accelerationx(self, ax):
        self.acceleration_x = 1 * ax 
    def accelerationy(self, ay):
        self.acceleration_y = 1 * ay   
        
    def speedx(self):
        self.speed_x = self.speed_x + self.acceleration_x
    def speedy(self):
        self.speed_y = self.speed_y + self.acceleration_y
        
    def pos_x(self):       
        self.x = self.x + self.speed_x
    def pos_y(self):
        self.y = self.y + self.speed_x

earth_mass_kg = 5.972 * 10 ** 24
earth_radius_km = 6371

earth = World(earth_mass_kg, earth_radius_km)
  
ball = Ball(0, 0)





i = 0
while i < 36:
    angle = math.radians(i * 10)
    angle_cos = math.cos(angle)
    angle_sin = math.sin(angle)
    
   
    
    ball.accelerationx(angle_cos)
    ball.accelerationy(angle_sin)
    ball.speedx()
    ball.speedy()
    ball.pos_x() 
    ball.pos_y() 
    print(angle_cos, angle_sin)
    
    
    i += 1
