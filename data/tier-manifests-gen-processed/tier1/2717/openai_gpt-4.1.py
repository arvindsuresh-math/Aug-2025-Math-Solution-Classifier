def solve():
    """Index: 2717.
    Returns: the total number of voters in Districts 1, 2, and 3.
    """
    # L1
    d1_voters = 322 # 322 voters in District 1

    # L2
    d3_multiplier = 2 # District 3 has twice as many voters as District 1
    d3_voters = d3_multiplier * d1_voters

    # L3
    d2_less_than_d3 = 19 # District 2 has 19 less voters than District 3
    d2_voters = d3_voters - d2_less_than_d3

    # L4
    total_voters = d1_voters + d2_voters + d3_voters

    # FA
    answer = total_voters
    return answer