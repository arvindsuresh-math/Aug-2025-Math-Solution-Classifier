def solve():
    """Index: 3762.
    Returns: the number of parking tickets Mark has.
    """
    # L1
    sarah_speeding_tickets = 6 # Sarah has 6 speeding tickets
    mark_speeding_tickets = 6 # they each have an equal number of speeding tickets
    total_speeding_tickets = sarah_speeding_tickets + mark_speeding_tickets

    # L2
    total_tickets = 24 # Mark and Sarah have 24 traffic tickets
    combined_parking_tickets = total_tickets - total_speeding_tickets

    # L3
    mark_parking_multiplier = 2 # Mark has twice as many parking tickets as Sarah

    # L6
    # The equation is m + s = combined_parking_tickets, and m = mark_parking_multiplier * s
    # So, (mark_parking_multiplier * s) + s = combined_parking_tickets
    # (mark_parking_multiplier + 1) * s = combined_parking_tickets
    # s = combined_parking_tickets / (mark_parking_multiplier + 1)
    mark_parking_multiplier_plus_one = mark_parking_multiplier + 1
    sarah_parking_tickets = combined_parking_tickets / mark_parking_multiplier_plus_one

    # L7
    mark_parking_tickets = sarah_parking_tickets * mark_parking_multiplier

    # FA
    answer = mark_parking_tickets
    return answer