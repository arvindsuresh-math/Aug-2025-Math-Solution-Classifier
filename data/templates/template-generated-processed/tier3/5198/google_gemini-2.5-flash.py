def solve():
    """Index: 5198.
    Returns: the total number of pairs of socks Lisa ended up with.
    """
    # L1
    sandra_socks = 20 # brought her 20 pairs of socks
    cousin_fraction_denominator = 5 # one-fifth the number of pairs that Sandra bought
    cousin_socks = sandra_socks / cousin_fraction_denominator

    # L2
    lisa_initial_socks = 12 # bought 12 pairs at a discount store
    mom_multiplier = 3 # three times the number of pairs Lisa started with
    three_times_lisa_socks = lisa_initial_socks * mom_multiplier

    # L3
    mom_additional_socks = 8 # 8 more than three times the number of pairs Lisa started with
    mom_socks = three_times_lisa_socks + mom_additional_socks

    # L4
    total_socks = lisa_initial_socks + sandra_socks + cousin_socks + mom_socks

    # FA
    answer = total_socks
    return answer