def solve():
    """Index: 1869.
    Returns: the amount of money Francie has remaining after buying the video game.
    """
    # L1
    allowance_week_1 = 5 # $5 a week
    weeks_1 = 8 # 8 weeks
    money_phase_1 = allowance_week_1 * weeks_1

    # L2
    allowance_week_2 = 6 # $6 a week
    weeks_2 = 6 # 6 weeks
    money_phase_2 = allowance_week_2 * weeks_2

    # L3
    total_money_saved = money_phase_1 + money_phase_2

    # L4
    clothes_fraction_denominator = 2 # half of the money
    money_after_clothes = total_money_saved / clothes_fraction_denominator

    # L5
    video_game_cost = 35 # video game that costs $35
    money_remaining = money_after_clothes - video_game_cost

    # FA
    answer = money_remaining
    return answer