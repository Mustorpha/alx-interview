#!/usr/bin/python3
"""0. Prime Game - Maria and Ben"""


def is_prime(num):
    """Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, else False.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determines the winner of each game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n for each round.

    Returns:
        str: The name of the player that won the most rounds, or None if it cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        maria_turn = True
        while primes:
            if maria_turn:
                for prime in primes:
                    if is_prime(prime):
                        primes = [i for i in primes if i % prime != 0]
                        break
                maria_turn = False
            else:
                for prime in primes:
                    if is_prime(prime):
                        primes = [i for i in primes if i % prime != 0]
                        break
                maria_turn = True
        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None