#!/usr/share/python3

def main():
    named_arguments(name = "Sebastian", address = "Spain", hobby = "Gaming")
    demarcation_line()
    another_named_arguments("Hi", 1235, 1, 2, 3, one = 1, two = 2, three = 3)
def named_arguments(**kwargs):
    for key in kwargs:
        print(key, "=", kwargs[key])

def another_named_arguments(arg1, arg2, *args, **kwargs):
    print(arg1, arg2)
    for index in args:
        print(index, end=" ")
    demarcation_line()
    for key in kwargs:
        print(key, "=", kwargs[key])
        
def demarcation_line():
    print("**********")        
        
if __name__ == "__main__":
    main()