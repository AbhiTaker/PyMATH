""" Module to perform arithmetic operation with modulo """

import math


def add(num1, num2, modulo):

    answer = ((num1 % modulo)+(num2 % modulo))%modulo

    return answer


def multiply(num1, num2, modulo):

    answer = ((num1 % modulo)*(num2 % modulo))%modulo
    
    return answer


def sub(num1, num2, modulo):

    answer = ( (num1 % modulo) - (num2 % modulo) + modulo )%modulo

    return answer


