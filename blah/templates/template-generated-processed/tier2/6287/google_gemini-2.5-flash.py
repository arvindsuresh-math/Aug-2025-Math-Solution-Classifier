def solve():
    """Index: 6287.
    Returns: the total money lost out a week by not being able to produce all the tires.
    """
    # L1
    cost_to_produce_tire = 250 # It cost $250 to produce each tire
    sales_multiplier = 1.5 # sell them for 1.5 times as much
    selling_price_per_tire = cost_to_produce_tire * sales_multiplier

    # L2
    profit_per_tire = selling_price_per_tire - cost_to_produce_tire

    # L3
    potential_production_capacity = 1200 # sell 1200 tires a day
    current_production = 1000 # produce 1000 tires a day
    production_shortfall = potential_production_capacity - current_production

    # L4
    daily_loss = profit_per_tire * production_shortfall

    # L5
    days_per_week = 7 # WK
    weekly_loss = daily_loss * days_per_week

    # FA
    answer = weekly_loss
    return answer