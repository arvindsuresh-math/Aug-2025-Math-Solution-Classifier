def solve():
    """Index: 3296.
    Returns: the total cost Ryan will pay for snacks.
    """
    # L1
    hours_to_work = 2 # 2 hours to work every day
    round_trip_multiplier = 2 # to work and back
    round_trip_hours = hours_to_work * round_trip_multiplier

    # L2
    multiplier_for_cost = 10 # Ten times the time
    cost_per_pack = round_trip_hours * multiplier_for_cost

    # L3
    num_packs = 50 # 50 packs of snacks
    total_cost = cost_per_pack * num_packs

    # FA
    answer = total_cost
    return answer