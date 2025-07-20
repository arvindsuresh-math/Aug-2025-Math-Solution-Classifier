def solve():
    """Index: 4409.
    Returns: the number of tins of beans left after damaged ones are thrown away.
    """
    # L1
    num_cases = 15 # 15 cases of tins of beans
    tins_per_case = 24 # Each case contains 24 tins
    total_tins_delivered = num_cases * tins_per_case

    # L2
    damaged_percent_decimal = 0.05 # 5% of the tins are damaged
    damaged_tins = total_tins_delivered * damaged_percent_decimal

    # L3
    tins_left = total_tins_delivered - damaged_tins

    # FA
    answer = tins_left
    return answer