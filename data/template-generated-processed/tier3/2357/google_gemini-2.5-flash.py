def solve():
    """Index: 2357.
    Returns: the total cost of Tim's birthday party.
    """
    # L1
    clown_hourly_cost = 100 # cost $100 an hour
    clown_hours = 4 # for 4 hours
    clown_total_cost = clown_hourly_cost * clown_hours

    # L2
    bounce_house_multiplier = 3 # 3 times as much an hour
    bounce_house_hourly_cost = clown_hourly_cost * bounce_house_multiplier

    # L3
    bounce_house_time_divisor = 2 # half the time
    bounce_house_hours = clown_hours / bounce_house_time_divisor

    # L4
    bounce_house_total_cost = bounce_house_hourly_cost * bounce_house_hours

    # L5
    other_costs = 1000 # Everything else for the party cost $1000
    total_cost = clown_total_cost + bounce_house_total_cost + other_costs

    # FA
    answer = total_cost
    return answer