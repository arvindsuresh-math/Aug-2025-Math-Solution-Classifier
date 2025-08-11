def solve():
    """Index: 2841.
    Returns: the number of additional tickets Dolly needs to buy.
    """
    # L1
    ferris_wheel_rides = 2 # ride the Ferris wheel twice
    ferris_wheel_cost_per_ride = 2 # Ferris wheel costs 2 tickets
    ferris_wheel_total_cost = ferris_wheel_rides * ferris_wheel_cost_per_ride

    # L2
    roller_coaster_rides = 3 # roller coaster three times
    roller_coaster_cost_per_ride = 5 # roller coaster costs 5 tickets
    roller_coaster_total_cost = roller_coaster_rides * roller_coaster_cost_per_ride

    # L3
    log_ride_rides = 7 # log ride seven times
    log_ride_cost_per_ride = 1 # log ride costs 1 ticket
    log_ride_total_cost = log_ride_rides * log_ride_cost_per_ride

    # L4
    total_tickets_needed = ferris_wheel_total_cost + roller_coaster_total_cost + log_ride_total_cost

    # L5
    tickets_dolly_has = 20 # Dolly has 20 tickets
    tickets_to_buy = total_tickets_needed - tickets_dolly_has

    # FA
    answer = tickets_to_buy
    return answer