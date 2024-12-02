#!/usr/share/python3

def main():
    for index in ReturnValue():
        print(index, end=" ")

def ReturnValue():
    # return "Returning string."
    # return 56
    return range(10)

if __name__ == "__main__":
    main()