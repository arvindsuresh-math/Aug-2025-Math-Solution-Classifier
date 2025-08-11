def solve():
    """Index: 5401.
    Returns: the amount Lyka should save per week.
    """
    # L1
    smartphone_cost = 160 # worth $160
    money_on_hand = 40 # she only has $40
    amount_to_save = smartphone_cost - money_on_hand

    # L2
    months_to_save = 2 # for two months
    weeks_per_month = 4 # WK
    total_weeks = months_to_save * weeks_per_month

    # L3
    weekly_saving = amount_to_save / total_weeks

    # FA
    answer = weekly_saving
    return answer