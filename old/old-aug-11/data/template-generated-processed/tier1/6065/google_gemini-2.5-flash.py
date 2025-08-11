def solve():
    """Index: 6065.
    Returns: the number of pencils left with Harry.
    """
    # L1
    anna_pencils = 50 # Anna has 50 pencils
    multiplier_twice = 2 # twice the number of Anna's Pencils
    harry_initial_pencils = anna_pencils * multiplier_twice

    # L2
    harry_lost = 19 # he lost 19 of them
    pencils_left_harry = harry_initial_pencils - harry_lost

    # FA
    answer = pencils_left_harry
    return answer