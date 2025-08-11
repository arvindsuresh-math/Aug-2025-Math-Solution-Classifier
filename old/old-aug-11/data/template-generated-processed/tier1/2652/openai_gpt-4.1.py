def solve():
    """Index: 2652.
    Returns: the amount of money the band still needs to earn to reach their goal.
    """
    # L1
    amount_per_family_10 = 10 # earned $10 each from three families
    num_families_10 = 3 # three families
    earned_10 = amount_per_family_10 * num_families_10

    # L2
    amount_per_family_5 = 5 # $5 each from 15 families
    num_families_5 = 15 # 15 families
    earned_5 = amount_per_family_5 * num_families_5

    # L3
    total_earned = earned_10 + earned_5

    # L4
    goal = 150 # Their goal is to collect $150
    amount_needed = goal - total_earned

    # FA
    answer = amount_needed
    return answer