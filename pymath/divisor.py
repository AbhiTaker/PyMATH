""" Module to deal with divisors """

import math


def count(num):
    """ function to find number of divisors O(n) """
    ctr = 2
    for i in range(2, num):
        if num % i == 0:
            ctr += 1
            
    return ctr

def div_list(num):
    """ function to return the list of divisors """
    div = []
    for i in range(1, num+1):
        if num % i == 0:
            div.append(i)
            
    return div


def gcd(num1, num2):
    """ function to return HCF of two numbers """
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

def lcm(num1, num2):
    """ function to return LCM of two numbers """
    answer = (num1*num2) / gcd(num1, num2)


def gcd_list(arr):
    """ function to return HCF of list of numbers """
    answer = arr[0]
    for i in arr:
        answer = gcd(answer, i)

    return answer

