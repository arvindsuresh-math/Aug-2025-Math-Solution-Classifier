def solve():
    """Index: 2717.
    Returns: the total number of voters in Districts 1 - 3.
    """
    # L1
    voters_district_1 = 322 # 322 voters in District 1

    # L2
    multiplier_d3 = 2 # twice as many voters
    voters_district_3 = multiplier_d3 * voters_district_1

    # L3
    voters_less_d2 = 19 # 19 less voters
    voters_district_2 = voters_district_3 - voters_less_d2

    # L4
    total_voters = voters_district_1 + voters_district_2 + voters_district_3

    # FA
    answer = total_voters
    return answer