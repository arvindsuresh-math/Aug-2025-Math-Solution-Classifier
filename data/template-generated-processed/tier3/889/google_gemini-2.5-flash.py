def solve():
    """Index: 889.
    Returns: the number of weeks Carrie has to work to purchase the iPhone.
    """
    # L1
    iphone_cost = 800 # The new iPhone costs $800
    trade_in_value = 240 # She can trade in her Samsung Galaxy for $240
    remaining_cost = iphone_cost - trade_in_value

    # L2
    earnings_per_week = 80 # She can make $80 per week babysitting
    weeks_to_work = remaining_cost / earnings_per_week

    # FA
    answer = weeks_to_work
    return answer