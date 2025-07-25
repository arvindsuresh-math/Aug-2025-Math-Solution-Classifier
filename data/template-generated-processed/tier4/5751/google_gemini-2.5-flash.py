def solve():
    """Index: 5751.
    Returns: the average number of extra chores Carol did each week.
    """
    # L1
    total_money = 425 # 425 dollars
    num_weeks = 10 # 10 weeks
    avg_money_per_week = total_money / num_weeks

    # L2
    fixed_allowance_per_week = 20 # fixed $20 allowance each week
    money_from_extra_chores_per_week = avg_money_per_week - fixed_allowance_per_week

    # L3
    money_per_extra_chore = 1.5 # $1.5 more dollars each week if she does extra chores
    avg_extra_chores_per_week = money_from_extra_chores_per_week / money_per_extra_chore

    # FA
    answer = avg_extra_chores_per_week
    return answer