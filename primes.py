"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import re

def primes(number_of_primes):
    list = []
    
    i = 2

    while len(list) < number_of_primes:
        if(re.match(r'^1?$|^(11+?)\1+$', '1' * i) == None):
            list.append(i)
            i +=1

    return list
