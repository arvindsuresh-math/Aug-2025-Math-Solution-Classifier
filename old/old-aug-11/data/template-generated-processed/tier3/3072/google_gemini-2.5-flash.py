def solve():
    """Index: 3072.
    Returns: the total number of crayons Martha has after the purchase.
    """
    # L1
    initial_crayons = 18 # Martha has 18 crayons
    half_divisor = 2 # lost half of them
    crayons_lost = initial_crayons / half_divisor

    # L2
    new_set_crayons = 20 # bought a new set of 20 crayons
    total_crayons = crayons_lost + new_set_crayons

    # FA
    answer = total_crayons
    return answer