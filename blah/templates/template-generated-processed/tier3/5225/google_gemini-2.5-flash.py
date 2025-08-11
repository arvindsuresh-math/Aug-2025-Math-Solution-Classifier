def solve():
    """Index: 5225.
    Returns: the total number of pens Bruno will have.
    """
    # L1
    dozen = 12 # WK
    num_dozens = 2 # two and one-half dozens
    two_dozens_pens = dozen * num_dozens

    # L2
    half_divisor = 2 # one-half dozens
    half_dozen_pens = dozen / half_divisor

    # L3
    total_pens = two_dozens_pens + half_dozen_pens

    # FA
    answer = total_pens
    return answer