def solve():
    """Index: 3287.
    Returns: the overall labor costs for one day.
    """
    # L1
    worker_daily_pay = 100 # construction workers each make $100/day
    electrician_multiplier = 2 # the electrician makes double what a worker is paid
    electrician_daily_pay = worker_daily_pay * electrician_multiplier

    # L2
    plumber_percentage_text = 250 # plumber makes 250% of a worker's salary
    plumber_percentage_value_in_calc = 250 # from solution text: 100*250*.01
    percent_factor = 0.01 # WK
    plumber_daily_pay = worker_daily_pay * plumber_percentage_value_in_calc * percent_factor

    # L3
    num_construction_workers = 2 # two construction workers
    construction_workers_total_pay = worker_daily_pay * num_construction_workers

    # L4
    total_labor_cost = electrician_daily_pay + plumber_daily_pay + construction_workers_total_pay

    # FA
    answer = total_labor_cost
    return answer