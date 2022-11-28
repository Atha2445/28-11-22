import sys


print(sys.getrecursionlimit())


def hello():
    print('Jai Hari')     
    hello()

hello()    