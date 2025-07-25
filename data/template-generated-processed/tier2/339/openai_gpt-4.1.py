def solve():
    """Index: 339.
    Returns: the number of pregnant female cows Terez has.
    """
    # L1
    total_cows = 44 # 44 cows on his farm
    female_percent = 0.50 # 50 percent of the cows are female
    num_females = total_cows * female_percent

    # L2
    pregnant_percent = 0.50 # 50 percent of the females are pregnant
    num_pregnant_females = num_females * pregnant_percent

    # FA
    answer = num_pregnant_females
    return answer