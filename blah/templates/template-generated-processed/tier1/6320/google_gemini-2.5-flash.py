def solve():
    """Index: 6320.
    Returns: the number of Bennett's brothers.
    """
    # L1
    aaron_brothers = 4 # Aaron has four brothers
    multiplier_twice = 2 # Twice
    twice_aaron_brothers = aaron_brothers * multiplier_twice

    # L2
    less_than_twice = 2 # two less than twice the number of Aaron's brothers
    bennett_brothers = twice_aaron_brothers - less_than_twice

    # FA
    answer = bennett_brothers
    return answer