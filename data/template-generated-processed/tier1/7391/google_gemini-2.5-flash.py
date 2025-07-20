def solve():
    """Index: 7391.
    Returns: the total amount Samantha spends.
    """
    # L1
    washer_cost_per_load = 4 # $4 for a washer
    num_loads = 2 # 2 loads of laundry
    washing_cost = washer_cost_per_load * num_loads

    # L2
    cost_per_quarter_cents = 25 # a quarter
    minutes_per_quarter_interval = 10 # every 10 minutes
    dryer_run_minutes_per_dryer = 40 # 40 minutes each
    num_intervals_per_dryer = dryer_run_minutes_per_dryer / minutes_per_quarter_interval
    cost_per_dryer_cents = cost_per_quarter_cents * num_intervals_per_dryer
    cost_per_dryer_dollars = 1 # 100 cents = $1

    # L3
    num_dryers = 3 # 3 separate dryers
    total_dryer_cost = cost_per_dryer_dollars * num_dryers

    # L4
    total_spent = washing_cost + total_dryer_cost

    # FA
    answer = total_spent
    return answer