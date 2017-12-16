""" Module to deal with divisors """

import math


def count(num):
    """ function to find number of divisors O(n) """
    ctr = 2

    for i in range(2, num):

        if num % i == 0:
            ctr += 1

    return ctr


    
