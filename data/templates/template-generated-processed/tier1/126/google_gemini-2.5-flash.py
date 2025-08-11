def solve():
    """Index: 126.
    Returns: the number of roommates John has.
    """
    # L1
    multiplier_twice = 2 # WK
    bob_roommates = 10 # Bob has 10 roommates
    twice_bob_roommates = multiplier_twice * bob_roommates

    # L2
    john_more_than_twice = 5 # five more roommates
    john_roommates = twice_bob_roommates + john_more_than_twice

    # FA
    answer = john_roommates
    return answer