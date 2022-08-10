import math

class Spherical:
    def __init__(self,radius):
        self.radius = radius
        
    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return math.pi*(4/3)*(self.radius**3)
    def findArea(self):
        return math.pi*4*(self.radius**2)
    # def radius(self):
    #     pass

    def __str__(self):
        return 'Radius ='+ str(self.radius) + ' Volumn = ' + str(self.findVolume()) + ' Area = ' + str(self.findArea())

r1,r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)