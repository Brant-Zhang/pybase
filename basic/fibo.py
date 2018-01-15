#!/usr/local/bin/python3

class Error(Exception):
    pass

class inputError(Error):
    def __init__(self,msg,exp):
        self.msg=msg
        self.exp=exp

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def herror():
    while True:
        try:
            x=int(input("input an number:"))
            break
        except ValueError:
            print("try again...")


if __name__ == "__main__":
    #import sys
    #fib(int(sys.argv[1]))
    xxx()
