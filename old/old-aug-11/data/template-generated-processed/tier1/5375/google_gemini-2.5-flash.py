def solve():
    """Index: 5375.
    Returns: the number of toys Jason has.
    """
    # L1
    john_more_than_rachel = 6 # 6 more toys than Rachel
    rachel_toys = 1 # Rachel has 1 toy
    john_toys = john_more_than_rachel + rachel_toys

    # L2
    jason_multiplier = 3 # three times as many toys as John
    jason_toys = jason_multiplier * john_toys

    # FA
    answer = jason_toys
    return answer