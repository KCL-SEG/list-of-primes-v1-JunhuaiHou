"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import re, sys

def primes(number_of_primes):
    list = []
    
    i = 2

    while len(list) < number_of_primes:
        #http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
        if(re.match(r'^1?$|^(11+?)\1+$', '1' * i) == None):
            list.append(i)
        
        i += 1

    return list

