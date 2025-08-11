def solve():
    """Index: 5739.
    Returns: the number of weeks Vanessa has to wait to buy the dress.
    """
    # L1
    dress_cost = 80 # costs $80
    initial_savings = 20 # already has $20 in savings
    money_needed = dress_cost - initial_savings

    # L2
    weekly_allowance = 30 # parents give her $30 every week
    weekly_spending = 10 # spends $10 each weekend
    net_weekly_gain = weekly_allowance - weekly_spending

    # L3
    weeks_to_wait = money_needed / net_weekly_gain

    # FA
    answer = weeks_to_wait
    return answer