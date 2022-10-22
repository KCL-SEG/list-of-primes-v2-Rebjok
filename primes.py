"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    list = [2]
    track = 1
    number = 3

    if number_of_primes <= 0:
        raise ValueError("Invalid Value: Please enter a number greater or equal to one.")


    while track < number_of_primes:

        is_prime = True
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                is_prime = False

        if is_prime:
            list.append(number)
            track += 1

        number += 2
    return list
