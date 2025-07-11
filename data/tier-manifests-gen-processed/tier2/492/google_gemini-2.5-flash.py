def solve():
    """Index: 492.
    Returns: the number of judges over 50 years old.
    """
    # L1
    total_judges = 40 # 40 Judges
    percent_under_30_decimal = 0.10 # 10 percent of Judges
    judges_under_30 = total_judges * percent_under_30_decimal

    # L2
    percent_30_to_50_decimal = 0.60 # 60 percent of Judges
    judges_30_to_50 = total_judges * percent_30_to_50_decimal

    # L3
    judges_over_50 = total_judges - judges_under_30 - judges_30_to_50

    # FA
    answer = judges_over_50
    return answer