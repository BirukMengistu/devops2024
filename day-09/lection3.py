#Property and Descriptor-Based Attributes
import constant
colors = constant.bcolors

class Circle:
    def __init__(self,radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2
   
    @diameter.setter
    def diameter(self,diameter):
        if not isinstance(diameter,int|float) or diameter <=0:
            raise ValueError('The diameter must be a non-negative real number')
        self.radius = diameter / 2
    @property
    def area(self):
        return 3.14159 * (self.radius ** 2)
    
#Test

circle = Circle(5)
circle.diameter = 4
print(f'circle.radius, {circle.radius}')

print(f'circle.diameter, {circle.diameter}')
print(f'{colors.OKGREEN }circle.area, {circle.area}')
print(f'{colors.ENDC}')
print('*'*50)