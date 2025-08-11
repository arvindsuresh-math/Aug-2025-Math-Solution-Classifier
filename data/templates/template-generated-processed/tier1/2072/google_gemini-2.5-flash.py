def solve():
    """Index: 2072.
    Returns: how many times faster than the first popsicle the last popsicle's remains melt.
    """
    # L1
    multiplier = 2 # twice as fast as the previous one
    first_popsicle_rate = 1 # WK
    second_popsicle_rate = multiplier * first_popsicle_rate

    # L2
    third_popsicle_rate = multiplier * second_popsicle_rate

    # L3
    fourth_popsicle_rate = multiplier * third_popsicle_rate

    # L4
    fifth_popsicle_rate = multiplier * fourth_popsicle_rate

    # L5
    sixth_popsicle_rate = multiplier * fifth_popsicle_rate

    # FA
    answer = sixth_popsicle_rate
    return answer