#!/usr/share/python3

class Robot:
    def __init__(self):
        pass
    def walk_like_a_robot(self):
        print("I walk like a robot")
    def care_like_a_robot(self):
        print("I care like a robot")
robu1 = Robot()
print(type(robu1))
print(id(robu1))
robu2 = Robot()
print(type(robu2))
print(id(robu2))
del robu2
def main():
    robu = Robot()
    print(type(robu))
    print(id(robu))
    
if __name__ == "__main__":
    main()