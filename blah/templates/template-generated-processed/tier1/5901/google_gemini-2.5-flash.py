def solve():
    """Index: 5901.
    Returns: the total number of tickets Janet needs.
    """
    # L1
    tickets_per_roller_coaster_ride = 5 # 5 tickets to ride the roller coaster
    roller_coaster_rides = 7 # roller coaster 7 times
    roller_coaster_total_tickets = tickets_per_roller_coaster_ride * roller_coaster_rides

    # L2
    tickets_per_giant_slide_ride = 3 # 3 tickets to ride the giant slide
    giant_slide_rides = 4 # giant slide 4 times
    giant_slide_total_tickets = tickets_per_giant_slide_ride * giant_slide_rides

    # L3
    total_tickets = giant_slide_total_tickets + roller_coaster_total_tickets

    # FA
    answer = total_tickets
    return answer