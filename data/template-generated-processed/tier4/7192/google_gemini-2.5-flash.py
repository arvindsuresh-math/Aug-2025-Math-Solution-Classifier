def solve():
    """Index: 7192.
    Returns: the number of pounds Bobby added per year to his deadlift.
    """
    # L1
    initial_deadlift = 300 # deadlift 300 pounds at 13
    percentage_factor = 2.5 # 250% of his previous deadlift
    increase_amount = 100 # 100 pounds more
    new_deadlift = initial_deadlift * percentage_factor + increase_amount

    # L2
    pounds_added_total = new_deadlift - initial_deadlift

    # L3
    age_later = 18 # When he is 18
    age_earlier = 13 # at 13
    years_passed = age_later - age_earlier

    # L4
    pounds_per_year = pounds_added_total / years_passed

    # FA
    answer = pounds_per_year
    return answer