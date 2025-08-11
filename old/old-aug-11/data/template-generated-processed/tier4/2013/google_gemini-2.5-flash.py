def solve():
    """Index: 2013.
    Returns: the number of slightly used crayons.
    """
    # L1
    total_crayons = 120 # 120 crayons in a box
    new_crayons_divisor = 3 # One third of the crayons are new
    new_crayons = total_crayons / new_crayons_divisor

    # L2
    broken_crayons_percent = 0.20 # 20% are broken
    broken_crayons = total_crayons * broken_crayons_percent

    # L3
    slightly_used_crayons = total_crayons - new_crayons - broken_crayons

    # FA
    answer = slightly_used_crayons
    return answer