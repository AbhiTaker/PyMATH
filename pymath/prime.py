""" Module to deal with functions related to prime numbers"""

import math

prime = []
""" range upto which you want to calculate prime """
MAX = int(1e6)

def __init__():
    """ intializing the prime list with true upto MAX"""
    
    for num in range(0,MAX+6):
            prime.append(True)


def sieve():
    """ function to find prime number efficently"""

    __init__()

    for num in range(2,MAX):

        if prime[num] == True:
            num2 = 2*num
            
            while num2 <= MAX:
                
                prime[num2] = False                          # composite number stores false value
                num2 += num 




def check_prime(num):
    """ primality check function """

    sieve() 
    """ calling sieve to store apt bool value in list[num] """

    if prime[num] == True :
        return True
    else :
        return False
        

def main():
    """ to test module functionality """

    sieve()
    num = input('Input a number: ')
    if prime[num]:
        print 'Number is prime'
    else:
        print 'Number is not prime'




if __name__=="__main__":
    main()
