def solve():
    """Index: 829.
    Returns: the number of additional tickets Jeanne should buy.
    """
    # L1
    ferris_wheel_tickets = 5 # Ferris wheel costs 5 tickets
    roller_coaster_tickets = 4 # roller coaster costs 4 tickets
    bumper_cars_tickets = 4 # bumper cars cost 4 tickets
    total_tickets_needed = ferris_wheel_tickets + roller_coaster_tickets + bumper_cars_tickets

    # L2
    jeanne_has = 5 # Jeanne has 5 tickets
    tickets_to_buy = total_tickets_needed - jeanne_has

    # FA
    answer = tickets_to_buy
    return answer