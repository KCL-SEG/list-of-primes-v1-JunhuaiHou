"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    for number in range(1, number_of_primes):
        for index in range(2, number):
            if(number % index == 0):
                break
        else:
            list.append(number)

    return list
