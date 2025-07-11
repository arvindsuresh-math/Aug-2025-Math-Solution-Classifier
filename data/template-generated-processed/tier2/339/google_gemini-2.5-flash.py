def solve():
    """Index: 339.
    Returns: the number of pregnant female cows Terez has.
    """
    # L1
    total_cows = 44 # 44 cows on his farm
    female_percent_decimal = 0.50 # 50 percent of the cows are female
    female_cows = total_cows * female_percent_decimal

    # L2
    pregnant_female_percent_decimal = 0.50 # 50 percent of the females are pregnant
    pregnant_female_cows = female_cows * pregnant_female_percent_decimal

    # FA
    answer = pregnant_female_cows
    return answer