#!usr/bin/python3

class Robot:
    def __init__(self):
        pass
    
    def walking_like_a_robot(self, style):
        self.style = style
        return self.style
    
    def care_like_a_robot(self):
        print("takes care like a robot.")
        
        
class Humans:
    def __init__(self, nature = "good"):
        self.nature = nature
        
    def good_human_being(self):
        print("need not repeat, a good human being is always", self.nature)
        
    def bad_human_being(self):
        self.nature = "need not repeat, bad human being is always bad."
        print(self.nature)
        
    def walking_like_a_robot(self, style):
        self.style = style
        return self.style

def main():
    robu = Robot()    
    robu.care_like_a_robot()
    print(robu.walking_like_a_robot("walks like a robot"))
    good_man = Humans()
    print(good_man.nature)
    good_man.good_human_being()
    bad_man = Humans()
    bad_man.nature = "bad"
    print(bad_man.nature)
    print(bad_man.walking_like_a_robot("he is human but walks like a robot"))
if __name__ == "__main__":
    main()        