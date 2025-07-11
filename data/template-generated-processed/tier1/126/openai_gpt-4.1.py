def solve():
    """Index: 126.
    Returns: the number of roommates John has.
    """
    # L1
    bob_roommates = 10 # Bob has 10 roommates
    twice = 2 # twice as many as Bob
    twice_bob = twice * bob_roommates

    # L2
    john_more_than_twice_bob = 5 # five more roommates than twice as many as Bob
    john_roommates = twice_bob + john_more_than_twice_bob

    # FA
    answer = john_roommates
    return answer