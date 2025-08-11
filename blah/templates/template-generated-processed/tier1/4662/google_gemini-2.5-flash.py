def solve():
    """Index: 4662.
    Returns: how much more money Zach needs to earn before he can buy the bike.
    """
    # L1
    babysitting_hours = 2 # babysitting for 2 hours
    babysitting_rate = 7 # $7 per hour to babysit
    babysitting_earnings = babysitting_hours * babysitting_rate

    # L2
    weekly_allowance = 5 # weekly allowance is $5
    lawn_mowing_pay = 10 # extra $10 to mow the lawn
    total_earnings_this_week = weekly_allowance + lawn_mowing_pay + babysitting_earnings

    # L3
    initial_savings = 65 # already saved up $65
    total_money_after_earnings = total_earnings_this_week + initial_savings

    # L4
    bike_cost = 100 # bike that costs $100
    money_needed = bike_cost - total_money_after_earnings

    # FA
    answer = money_needed
    return answer