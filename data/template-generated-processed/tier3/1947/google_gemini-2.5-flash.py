def solve():
    """Index: 1947.
    Returns: the total number of jellybeans Caleb and Sophie have.
    """
    # L1
    caleb_dozens = 3 # 3 dozen jellybeans
    jellybeans_per_dozen = 12 # WK
    caleb_total_jellybeans = caleb_dozens * jellybeans_per_dozen

    # L2
    sophie_divisor = 2 # half as many jellybeans
    sophie_total_jellybeans = caleb_total_jellybeans / sophie_divisor

    # L3
    total_jellybeans = caleb_total_jellybeans + sophie_total_jellybeans

    # FA
    answer = total_jellybeans
    return answer