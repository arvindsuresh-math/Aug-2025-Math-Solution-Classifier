def solve():
    """Index: 6617.
    Returns: the percent increase in the cost of each ticket.
    """
    # L1
    current_cost = 102 # This year, it costs $102
    last_year_cost = 85 # Last year, opera seating cost $85 per ticket
    price_increase = current_cost - last_year_cost

    # L2
    percentage_multiplier = 100 # x 100%
    percent_increase = (price_increase / last_year_cost) * percentage_multiplier

    # FA
    answer = percent_increase
    return answer