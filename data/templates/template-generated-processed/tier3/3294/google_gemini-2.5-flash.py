def solve():
    """Index: 3294.
    Returns: the total number of cows the rancher will own after two years.
    """
    # L1
    initial_cows = 200 # 200 cows
    growth_divisor = 2 # half the number of cows
    calves_born_year1 = initial_cows / growth_divisor
    cows_after_one_year = initial_cows + calves_born_year1

    # L2
    calves_born_year2 = cows_after_one_year / growth_divisor
    cows_after_two_years = cows_after_one_year + calves_born_year2

    # FA
    answer = cows_after_two_years
    return answer