def solve():
    """Index: 3591.
    Returns: the current worth of Pima's investment.
    """
    # L1
    initial_investment = 400 # invested $400
    first_week_gain_percent_num = 25 # gained 25% in value
    percent_factor = 0.01 # WK
    first_week_gain_amount = initial_investment * first_week_gain_percent_num * percent_factor

    # L2
    value_after_first_week = initial_investment + first_week_gain_amount

    # L3
    second_week_gain_percent_num = 50 # gained an additional 50%
    second_week_gain_amount = value_after_first_week * second_week_gain_percent_num * percent_factor

    # L4
    final_investment_worth = value_after_first_week + second_week_gain_amount

    # FA
    answer = final_investment_worth
    return answer