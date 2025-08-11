def solve():
    """Index: 1657.
    Returns: the total house rent.
    """
    # L1
    rose_share = 1800 # Rose’s share is $1,800
    purity_share_divisor = 3 # thrice what Purity pays
    purity_share = rose_share / purity_share_divisor

    # L2
    sheila_multiplier = 5 # five times Purity’s share
    sheila_share = sheila_multiplier * purity_share

    # L3
    total_rent = purity_share + sheila_share + rose_share

    # FA
    answer = total_rent
    return answer