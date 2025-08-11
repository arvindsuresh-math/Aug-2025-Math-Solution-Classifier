def solve():
    """Index: 6518.
    Returns: the total number of pants Dani will have in 5 years.
    """
    # L1
    pairs_per_year = 4 # 4 pairs of two pants each
    pants_per_pair = 2 # WK
    pants_per_year = pairs_per_year * pants_per_pair

    # L2
    num_years = 5 # in 5 years
    total_pants_received = num_years * pants_per_year

    # L3
    initial_pants = 50 # initially had 50 pants
    final_pants = initial_pants + total_pants_received

    # FA
    answer = final_pants
    return answer