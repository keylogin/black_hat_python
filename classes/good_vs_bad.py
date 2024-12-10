#!usr/bin/python3

class Robots:
    
    def __init__(self):
        pass
    
    def walk_like_a_robot(self, walking_style):
        self.walking_style = walking_style
        return self.walking_style
    
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
    
    def walk_like_a_robot(self, walking_style):
        self.walking_style = walking_style
        return self.walking_style
    
def main():
    robu = Robots()
    # robu.care_like_a_robot()
    # print(robu.walk_like_a_robot("A robot walks like a robot and nothing happens."))
    good_man = Humans()
    # print(good_human.nature)
    # good_man.good_human_being()
    bad_man = Humans()
    # bad_man.nature = "bad"
    # print(bad_man.nature)
    # bad_man.bad_human_being()
    # print(bad_man.walk_like_a_robot("he is human but walks like a robot"))
    # when a bad man walks like a robot many thinks happen
    when_a_bad_man_walks_like_a_robot = bad_man.walk_like_a_robot(dict(change = "he becomes a monster inside", 
                                                                       act = "he kills fellow people",
                                                                       feel = "he enjoys torturing animals",
                                                                       care = "he cares for none",
                                                                       look = "he looks a normal human being",
                                                                       state = "finally he destroys himself"))
    # there are lot of actions that take place
    print("What happens when a bad man walks like a Robot?")
    
    change = input("Tell us what kind of change may take place inside him?\n Choose between 'monster' and 'angel', "               "and type here...>>>>")
    when_a_bad_man_walks_like_a_robot['change'] = change
    reward = 0
    if change == "monster":
        print("You have won the first round:", change)
        reward = 1000
        print("You have won ", reward, "points.")
        print("What does he do? :", when_a_bad_man_walks_like_a_robot['act'])
        
        change = input("Now tell us what the monster feels inside while killing people?\n Choose between 'great' and 'sad',""and type here...>>>>")
        when_a_bad_man_walks_like_a_robot['change'] = change
        if change == "great":
            print("You have won the second round:")
            reward = 10000
            print("You have won ", reward, "points.")
            print("What does he do? :", when_a_bad_man_walks_like_a_robot['feel'])   
            
            change = input("Tell us does the monster care for anyone?\n Choose between 'yes' and 'no',""and type here...>>>>")
            if change == "no":
                print("You have won the third round:")
                reward = 100000
                print("You have won ", reward, "points.")
                print("What does he do? :", when_a_bad_man_walks_like_a_robot['care'])
                change = input("Tell us does the monster look like a normal human being?\n Choose between 'yes' and 'no',""and type here...>>>>")
                if change == "yes":
                    print("You have won the fourth round:")
                    reward = 1000000
                    print("You have won ", reward, "points.")
                    print("What does he do? :", when_a_bad_man_walks_like_a_robot['look'])
                    
                    change = input("Tell us what happens to the monster finally?\n Doaes he destroy himself\n Choose between 'yes' and 'no',""and type here...>>>>")
                    when_a_bad_man_walks_like_a_robot['change'] = change
                    if change == "yes":
                        print("You have won the fifth round:")
                        reward = 10000000
                        print("You have won Jackpot.", reward, "points.")
                    else:
                        print("You have changed the course of game. It ends here. You have lost", reward - 100000, "points.")
                else:
                    print("You have changed the course of game. It ends here. You have lost", reward - 1000, "points.")     
            else:
                print("You have changed the course of game. It ends here. You have lost", reward - 100, "points.")
        else:
            print("You have changed the course of game. It ends here. You have lost", reward - 10, "points.")
    else:
        print("You have changed the course of game. It ends here and you have won no points.")

if __name__ == "__main__":
    main()        
                