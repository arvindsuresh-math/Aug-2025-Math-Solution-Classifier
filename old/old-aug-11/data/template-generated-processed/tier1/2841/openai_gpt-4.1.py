def solve():
    """Index: 2841.
    Returns: the number of additional tickets Dolly should buy.
    """
    # L1
    ferris_rides = 2 # ride the Ferris wheel twice
    ferris_cost = 2 # Ferris wheel costs 2 tickets
    ferris_total = ferris_rides * ferris_cost

    # L2
    coaster_rides = 3 # roller coaster three times
    coaster_cost = 5 # roller coaster costs 5 tickets
    coaster_total = coaster_rides * coaster_cost

    # L3
    log_rides = 7 # log ride seven times
    log_cost = 1 # log ride costs 1 ticket
    log_total = log_rides * log_cost

    # L4
    total_needed = ferris_total + coaster_total + log_total

    # L5
    dolly_tickets = 20 # Dolly has 20 tickets
    tickets_to_buy = total_needed - dolly_tickets

    # FA
    answer = tickets_to_buy
    return answer