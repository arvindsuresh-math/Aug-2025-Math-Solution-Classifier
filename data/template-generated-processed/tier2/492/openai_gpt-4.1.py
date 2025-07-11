def solve():
    """Index: 492.
    Returns: the number of Judges in Rhode Island who are over 50 years old.
    """
    # L1
    total_judges = 40 # 40 Judges in the state of Rhode Island
    under_30_percent = 0.10 # 10 percent of Judges are under 30 years old
    under_30_count = total_judges * under_30_percent

    # L2
    between_30_50_percent = 0.60 # 60 percent of Judges are 30-50 years old
    between_30_50_count = total_judges * between_30_50_percent

    # L3
    over_50_count = total_judges - under_30_count - between_30_50_count

    # FA
    answer = over_50_count
    return answer