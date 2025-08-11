def solve():
    """Index: 3243.
    Returns: the total number of apples Grace will have after 6 weeks.
    """
    # L1
    bella_apples_per_day = 6 # Bella eats 6 apples a day
    days_per_week = 7 # WK
    bella_apples_per_week = bella_apples_per_day * days_per_week

    # L2
    fraction_consumed_by_bella_denominator = 3 # a third of the apples Grace picks
    grace_apples_per_week = bella_apples_per_week * fraction_consumed_by_bella_denominator

    # L3
    grace_leftover_per_week = grace_apples_per_week - bella_apples_per_week

    # L4
    num_weeks = 6 # after 6 weeks
    total_apples_grace_has = grace_leftover_per_week * num_weeks

    # FA
    answer = total_apples_grace_has
    return answer