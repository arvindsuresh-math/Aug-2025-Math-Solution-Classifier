def solve():
    """Index: 4946.
    Returns: the number of seeds in bucket C.
    """
    # L1
    more_seeds_A_than_B = 10 # ten more seeds in bucket A than in bucket B
    seeds_in_B = 30 # bucket B has 30 seeds
    seeds_in_A = more_seeds_A_than_B + seeds_in_B

    # L2
    seeds_in_A_and_B = seeds_in_A + seeds_in_B

    # L3
    total_seeds = 100 # 100 seeds
    seeds_in_C = total_seeds - seeds_in_A_and_B

    # FA
    answer = seeds_in_C
    return answer