""" Module to deal with functions related to prime numbers"""

import math

isPrime = []
""" range upto which you want to calculate prime """
MAX = int(1e6)

def __init__():
    """ intializing the prime list with True value upto MAX"""
    
    for num in range(0,MAX+6):
            isPrime.append(True)


def sieve():
    """ function to find prime number efficiently"""

    __init__()

    for num in range(2,MAX):

        if isPrime[num] == True:
            num2 = 2*num
            
            while num2 <= MAX:
                
                isPrime[num2] = False                          # composite number marked false
                num2 += num 




def check_prime(num):
    """ primality check function """

    sieve() 
    """ calling sieve to store apt bool value in list[num] """

    if isPrime[num] == True :
        return True
    else :
        return False
        

def main():
    """ to test module functionality """

    sieve()
    num = input('Input a number: ')
    if isPrime[num]:
        print 'Number is prime'
    else:
        print 'Number is not prime'




if __name__=="__main__":
    main()
