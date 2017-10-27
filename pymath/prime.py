""" Module to deal with functions related to prime numbers"""

import math

isPrime = []
""" range upto which you want to calculate prime """
MAX = int(1e6)
Factor = []

def __init__():
    """ intializing the prime list with True value upto MAX"""
    for num in range(0, MAX+6):
            isPrime.append(True)
            Factor.append(0)



def sieve():
    """ function to find prime number efficiently"""

    __init__()

    for num in range(2, MAX):
        if isPrime[num]:
            num2 = 2*num
            
            while num2 <= MAX:
                isPrime[num2] = False                        # composite number marked false
                Factor[num2] += 1
                num2 += num




def check_prime(num):
    """ primality check function """

    sieve()

    return isPrime[num]
        
def factor_count(num):
    """ to count prime Factors of a number """

    sieve()
    return Factor[num]



def main():
    """ to test module functionality """

    num = input('Input a number: ')
    print(factor_count(num))
    if isPrime[num]:
        print 'Number is prime'
    else:
        print 'Number is not prime'




if __name__ == "__main__":
    main()
