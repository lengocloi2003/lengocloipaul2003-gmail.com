import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n','--name',default= 'Мир')

    return parser

def fibo(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    print (fibo(int(namespace.name)))