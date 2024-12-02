#!/usr/bin/python3

def main():
    passing_parameters(1, 12)

def passing_parameters(argument1, argument2 = None, argument3 = 6):
    if argument2 == None:    
        print("Here is our arguments: ", argument1, argument2, argument3)
    else:
        print("Here is our arguments: ", argument1, argument2, argument3)
if __name__ == "__main__":
    main()