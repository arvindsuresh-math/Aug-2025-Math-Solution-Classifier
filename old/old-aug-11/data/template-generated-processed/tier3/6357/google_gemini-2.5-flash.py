def solve():
    """Index: 6357.
    Returns: the number of weeks it will take Nina to buy the new video game.
    """
    # L1
    tax_percentage_numerator = 10 # 10 percent sales tax
    tax_percentage_denominator = 100 # 10 percent sales tax
    game_cost = 50 # The game cost 50 dollars
    tax_amount = (tax_percentage_numerator / tax_percentage_denominator) * game_cost

    # L2
    total_cost = game_cost + tax_amount

    # L3
    weekly_allowance = 10 # 10 dollars a week as an allowance
    saving_divisor = 2 # save half of that
    weekly_savings = weekly_allowance / saving_divisor

    # L4
    weeks_needed = total_cost / weekly_savings

    # FA
    answer = weeks_needed
    return answer