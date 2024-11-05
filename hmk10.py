#WEEK 10  
#1
'''
1-True
2-False
3-False
4-False
5-False
6-True
7-False
8-False
9-False
10-True

'''
#2

'''
1-B
2-B
3-D
4-B
5-C
'''


#3

#Instance variables and regular function variables both store data, but they serve different purposes. Instance variables are tied to a specific object and are created inside a class using `self`. These variables stick around for as long as the object does, and any method in the class can access them. In contrast, regular function variables are created inside a function and only exist while the function is running. Once the function finishes, those variables are gone and can’t be accessed anymore. So, instance variables are used to store information about the object itself, while function variables are just temporary data used during a function’s execution.

#4

import math

class Sphere:
    def __init__(self, radius):
        """Creates a sphere with the given radius."""
        self.radius = radius

    def getRadius(self):
        """Returns the radius of the sphere."""
        return self.radius

    def surfaceArea(self):
        """Calculates and returns the surface area of the sphere."""
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        """Calculates and returns the volume of the sphere."""
        return (4 / 3) * math.pi * (self.radius ** 3)

def main():
    radius = float(input("Enter the radius of the sphere: "))
    
    sphere = Sphere(radius)
    
    print(f"Radius: {sphere.getRadius()}")
    print(f"Surface Area: {sphere.surfaceArea():.2f}")
    print(f"Volume: {sphere.volume():.2f}")

if __name__ == "__main__":
    main()
