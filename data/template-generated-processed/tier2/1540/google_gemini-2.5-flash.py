def solve():
    """Index: 1540.
    Returns: the total amount of money Sam has now.
    """
    # L1
    initial_investment = 10000 # Sam invested $10,000
    interest_factor_compounded = 1.2 # earned 20% interest compounded
    investment_after_year1 = initial_investment * interest_factor_compounded

    # L2
    investment_after_year2 = investment_after_year1 * interest_factor_compounded

    # L3
    investment_after_year3 = investment_after_year2 * interest_factor_compounded

    # L4
    times_multiplier = 3 # three times as much invested
    investment_after_additional_investment = times_multiplier * investment_after_year3

    # L5
    return_factor_next_year = 1.15 # 15% return on his investment
    final_money = investment_after_additional_investment * return_factor_next_year

    # FA
    answer = final_money
    return answer