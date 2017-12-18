""" Module to perform arithmetic operation with modulo """

import math


def modInverse(num, mod):
    """ function to return multiplicative modulo inverse of num & mod """

    num = num % mod

    for i in range(1, mod):
        if (num * i) % mod == 1:
            return i


def add(num1, num2, mod):
    """ adding 2 numbers & taking their modulo """

    answer = ((num1 % mod)+(num2 % mod))%mod

    return answer


def multiply(num1, num2, mod):
    """ multiplying 2 numbers & taking their modulo """

    answer = ((num1 % mod)*(num2 % mod))%mod
    
    return answer


def sub(num1, num2, modulo):
    """ subtracting 2 numbers & taking their modulo """

    answer = ( (num1 % mod) - (num2 % mod) + mod )%mod

    return answer


def div(num1, num2, mod):
    """ function to divide two numbers and taking their modulo """

    inv_num2 =  modInverse(num2, mod)                               #multiplicative modulo inverse of num2 and modulo 

    answer = ( (num1 % mod)*(inv_num2 % mod) )%mod


print(modInverse(5,12))
