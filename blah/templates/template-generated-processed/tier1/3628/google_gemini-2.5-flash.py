def solve():
    """Index: 3628.
    Returns: the total amount Edmund earns from extra chores.
    """
    # L1
    num_weeks_total = 2 # two weeks
    normal_chores_per_week = 12 # 12 chores a week
    normal_chores_two_weeks = num_weeks_total * normal_chores_per_week

    # L2
    days_in_week = 7 # WK
    chores_per_day_extra = 4 # 4 chores a day
    total_chores_per_week_new = days_in_week * chores_per_day_extra

    # L3
    total_chores_two_weeks_new = num_weeks_total * total_chores_per_week_new

    # L4
    extra_chores_done = total_chores_two_weeks_new - normal_chores_two_weeks

    # L5
    pay_per_extra_chore = 2 # $2 for every extra chore
    total_earnings = pay_per_extra_chore * extra_chores_done

    # FA
    answer = total_earnings
    return answer