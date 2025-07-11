def solve():
    """Index: 1285.
    Returns: the total number of surfers on the two beaches.
    """
    # L1
    surfers_santa_monica = 20 # 20 surfers in Santa Monica
    multiplier_malibu = 2 # twice as many surfers
    surfers_malibu = multiplier_malibu * surfers_santa_monica

    # L2
    total_surfers = surfers_malibu + surfers_santa_monica

    # FA
    answer = total_surfers
    return answer