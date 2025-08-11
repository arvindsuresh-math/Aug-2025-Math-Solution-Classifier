def solve():
    """Index: 3082.
    Returns: the number of seashells Leigh had.
    """
    # L1
    mimi_dozens = 2 # 2 dozen seashells
    shells_per_dozen = 12 # WK
    mimi_shells = mimi_dozens * shells_per_dozen

    # L2
    kyle_multiplier = 2 # twice as many shells as Mimi
    kyle_shells = mimi_shells * kyle_multiplier

    # L3
    leigh_divisor = 3 # one-third of the shells
    leigh_shells = kyle_shells / leigh_divisor

    # FA
    answer = leigh_shells
    return answer