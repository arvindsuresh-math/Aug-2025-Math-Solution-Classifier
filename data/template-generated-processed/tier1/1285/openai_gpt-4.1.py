def solve():
    """Index: 1285.
    Returns: the total number of surfers on Malibu and Santa Monica beaches.
    """
    # L1
    santa_monica_surfers = 20 # 20 surfers in Santa Monica
    malibu_multiplier = 2 # twice as many surfers on Malibu beach
    malibu_surfers = malibu_multiplier * santa_monica_surfers

    # L2
    total_surfers = malibu_surfers + santa_monica_surfers

    # FA
    answer = total_surfers
    return answer