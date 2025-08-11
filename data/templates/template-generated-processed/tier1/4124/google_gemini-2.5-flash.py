def solve():
    """Index: 4124.
    Returns: the total amount of water filled in the pool after 3 trips each.
    """
    # L1
    tina_pail_capacity = 4 # Tina's is 4 gallons
    tommy_more_than_tina = 2 # Tommy's holds 2 gallons more than Tina's
    tommy_pail_capacity = tina_pail_capacity + tommy_more_than_tina

    # L2
    timmy_multiplier = 2 # twice as much water
    timmy_pail_capacity = tommy_pail_capacity * timmy_multiplier

    # L3
    gallons_per_trip = tina_pail_capacity + tommy_pail_capacity + timmy_pail_capacity

    # L4
    num_trips = 3 # after 3 trips each
    total_gallons = gallons_per_trip * num_trips

    # FA
    answer = total_gallons
    return answer