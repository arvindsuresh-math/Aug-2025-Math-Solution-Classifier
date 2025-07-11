def solve():
    """Index: 2754.
    Returns: the number of oranges Emily has.
    """
    # L1
    sandra_multiplier = 3 # Sandra has 3 times as many oranges as Betty
    betty_oranges = 12 # Betty has 12 oranges
    sandra_oranges = sandra_multiplier * betty_oranges

    # L2
    emily_multiplier = 7 # Emily has 7 times as many oranges as Sandra
    emily_oranges = emily_multiplier * sandra_oranges

    # FA
    answer = emily_oranges
    return answer