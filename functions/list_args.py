#!/usr/share/python3

def main():
    passing_list_of_arguments(1, 2, 3, 5, 7, 45, 98, 56, 4356, 90876543)
    passing_another_list_of_arguments(1, 2, 3, 5, 7, 45, 98, 76, 987654, 3245, 2345, 98760)
    
def passing_list_of_arguments(arg1, arg2, arg3, arg4, *args):
    print(arg1, arg2, arg3, arg4, args)
    
def passing_another_list_of_arguments(param1, param2, *params):
    print(param1, param2)
    for index in params:
        if index == 76:
            x = 10
            y = index + x
            print("We are going to add 10 with", index, "and the new value is:", y)
            continue
        print(index, end=" ")
        
if __name__ == "__main__":
    main()