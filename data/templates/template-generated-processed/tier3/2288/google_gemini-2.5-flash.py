def solve():
    """Index: 2288.
    Returns: the total number of marbles Alex has.
    """
    # L1
    ratio_brittany = 3 # ratio 3:5:7
    ratio_alex = 5 # ratio 3:5:7
    ratio_jamy = 7 # ratio 3:5:7
    total_ratio_parts = ratio_brittany + ratio_alex + ratio_jamy

    # L2
    total_marbles = 600 # 600 marbles
    brittany_marbles = (ratio_brittany / total_ratio_parts) * total_marbles

    # L3
    alex_initial_marbles = (ratio_alex / total_ratio_parts) * total_marbles

    # L4
    half_fraction_numerator = 1 # half of her marbles
    half_fraction_denominator = 2 # half of her marbles
    marbles_from_brittany = (half_fraction_numerator / half_fraction_denominator) * brittany_marbles

    # L5
    alex_total_marbles = alex_initial_marbles + marbles_from_brittany

    # FA
    answer = alex_total_marbles
    return answer