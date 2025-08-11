def solve():
    """Index: 3405.
    Returns: the total cost to fix all shirts and pants.
    """
    # L1
    num_shirts = 10 # 10 shirts
    hours_per_shirt = 1.5 # 1.5 hours to fix a shirt
    total_shirt_hours = num_shirts * hours_per_shirt

    # L2
    pants_time_multiplier = 2 # twice as long
    hours_per_pair_of_pants = hours_per_shirt * pants_time_multiplier

    # L3
    num_pants = 12 # 12 pairs of pants
    total_pants_hours = hours_per_pair_of_pants * num_pants

    # L4
    total_hours = total_shirt_hours + total_pants_hours

    # L5
    hourly_rate = 30 # $30 per hour
    total_cost = total_hours * hourly_rate

    # FA
    answer = total_cost
    return answer