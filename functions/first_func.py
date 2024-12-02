#!/usr/bin/python3
import math
def main():
    print("Hello World")
    
    
def DemarcationLine():
    print("This is a demarcation line")

def sum(a, b):
    return a + b

def Coordonates(x, y, z):
    cos_x = math.cos(x)
    sin_y = math.sin(y)
    tan_z = math.tan(z)
    return cos_x, sin_y, tan_z, x, y, z

# Functions can call other functions
def AnotherFunction():
    print("This is another function")
    


# Functions can call other functions
def TestFunction():
    print("This is a test function")
    AnotherFunction()

    
    
if __name__ == "__main__":
    main()
    DemarcationLine()
    DemarcationLine()
    print(sum(10, 20))
    print(Coordonates(3.14, 2.71, 1.57))
    # Functions can call other functions
    TestFunction()
    # Functions can call other functions
    AnotherFunction()