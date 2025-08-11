def solve():
    """Index: 829.
    Returns: the number of additional tickets Jeanne should buy.
    """
    # L1
    ferris_wheel_cost = 5 # The Ferris wheel costs 5 tickets
    roller_coaster_cost = 4 # the roller coaster costs 4 tickets
    bumper_cars_cost = 4 # the bumper cars cost 4 tickets
    total_tickets_needed = ferris_wheel_cost + roller_coaster_cost + bumper_cars_cost

    # L2
    tickets_jeanne_has = 5 # Jeanne has 5 tickets
    tickets_to_buy = total_tickets_needed - tickets_jeanne_has

    # FA
    answer = tickets_to_buy
    return answer