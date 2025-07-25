def solve():
    """Index: 5943.
    Returns: the number of grape lollipops.
    """
    # L1
    total_lollipops = 42 # 42 lollipops
    half_divisor = 2 # Half of the lollipops
    not_cherry_lollipops = total_lollipops / half_divisor

    # L2
    grape_divisor = 3 # 1/3 of them were grape
    grape_lollipops = not_cherry_lollipops / grape_divisor

    # FA
    answer = grape_lollipops
    return answer