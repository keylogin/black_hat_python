#!/usr/share/python3

def main():
    # for index in RangeFunction(15, 1025, 102):
    #     print(index, end=" ")
    for index in another_range_function(10, 2500):
        print(index, end=" ")   
# def RangeFunction(start, stop, step):
#     i = start
#     while i <= stop:
#         yield i
#         i += step

def another_range_function(*args):
    number_of_arguments = len(args)
    
    if number_of_arguments < 1: raise TypeError("At least one argument is required.")
    elif number_of_arguments == 1:
        stop = args[0]
        start = 0
        step = 1
    elif number_of_arguments == 2:
        # start and stop will be tuple
        (start, stop) = args
        step = 1
    elif number_of_arguments == 3:
        # all start and stop and step will be tuple
        (start, stop, step) = args
        
    i = start
    while i <= stop:
        yield i
        i += step
    
if __name__ == "__main__":
    main()