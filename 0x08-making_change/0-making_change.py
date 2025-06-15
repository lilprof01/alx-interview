#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """Determines the fewest number of 'coins' needed to meet 'total'

    Args:
        coins [list]: A list of values of coins in possessions
        total (int): Target amount

    Return:
        coins: The fewest number of coins to meet 'total
        0: If 'total' is 0 or less
        -1: If total cannot be met by any number of 'coins'
    """
    counted = tally = 0

    if total < 1:
        return 0

    for coin in sorted(coins)[::-1]:
        while counted + coin <= total:
            counted += coin
            tally += 1

    if counted != total:
        return -1

    return tally
