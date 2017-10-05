""" Module to perform arithmetic operation with modulo """

import math


def add(num1, num2, modulo):
    """ adding 2 numbers & taking their modulo """

    answer = ((num1 % modulo)+(num2 % modulo))%modulo

    return answer


def multiply(num1, num2, modulo):
    """ multiplying 2 numbers & taking their modulo """

    answer = ((num1 % modulo)*(num2 % modulo))%modulo
    
    return answer


def sub(num1, num2, modulo):
    """ subtracting 2 numbers & taking their modulo """

    answer = ( (num1 % modulo) - (num2 % modulo) + modulo )%modulo

    return answer


