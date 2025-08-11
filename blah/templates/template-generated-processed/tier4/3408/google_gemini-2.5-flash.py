def solve():
    """Index: 3408.
    Returns: the cost in dollars to run the computer for 50 hours.
    """
    # L1
    old_computer_watts = 800 # 800 watts
    new_computer_more_percent = 0.5 # 50% more
    new_computer_more_watts = old_computer_watts * new_computer_more_percent

    # L2
    new_computer_total_watts = old_computer_watts + new_computer_more_watts

    # L3
    watts_per_kilowatt = 1000 # WK
    new_computer_kw = new_computer_total_watts / watts_per_kilowatt

    # L4
    old_electricity_price_cents = 12 # 12 cents per kilowatt-hour
    electricity_price_increase_percent = 0.25 # went up by 25%
    electricity_price_increase_cents = old_electricity_price_cents * electricity_price_increase_percent

    # L5
    new_electricity_price_cents = old_electricity_price_cents + electricity_price_increase_cents

    # L6
    run_hours = 50 # run for 50 hours
    total_kwh_used = new_computer_kw * run_hours

    # L7
    total_cost_cents = new_electricity_price_cents * total_kwh_used

    # L8
    cents_per_dollar = 100 # WK
    total_cost_dollars = total_cost_cents / cents_per_dollar

    # FA
    answer = total_cost_dollars
    return answer