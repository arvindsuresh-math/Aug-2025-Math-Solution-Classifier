def solve():
    """Index: 6277.
    Returns: the number of goats Ahmed has.
    """
    # L1
    andrew_more_than_twice = 5 # 5 more than twice as many goats
    andrew_multiplier = 2 # twice as many goats
    adam_goats = 7 # Adam has 7 goats
    andrew_goats = andrew_more_than_twice + andrew_multiplier * adam_goats

    # L2
    ahmed_fewer_than_andrew = 6 # 6 fewer goats than Andrew
    ahmed_goats = andrew_goats - ahmed_fewer_than_andrew

    # FA
    answer = ahmed_goats
    return answer