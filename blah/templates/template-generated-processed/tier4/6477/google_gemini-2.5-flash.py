def solve():
    """Index: 6477.
    Returns: the number of houses Jackson needs to visit per day on the remaining days.
    """
    # L1
    weekly_goal = 1000 # $1000 for the week
    earned_monday = 300 # $300 on Monday
    earned_tuesday = 40 # $40 on Tuesday
    amount_needed = weekly_goal - earned_monday - earned_tuesday

    # L2
    total_workdays_week = 5 # 5 days a week
    days_already_worked = 2 # on Monday and on Tuesday
    remaining_workdays = total_workdays_week - days_already_worked

    # L3
    amount_per_day = amount_needed / remaining_workdays

    # L4
    money_per_group_of_houses = 10 # $10 for every 4 houses
    houses_per_group = 4 # 4 houses
    money_per_house = money_per_group_of_houses / houses_per_group

    # L5
    houses_per_day = amount_per_day / money_per_house

    # FA
    answer = houses_per_day
    return answer