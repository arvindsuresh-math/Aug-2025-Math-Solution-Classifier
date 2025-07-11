def solve():
    """Index: 2785.
    Returns: the total cost of the wedding.
    """
    # L1
    john_guests = 50 # John wants 50 guests
    wife_more_percent = 0.6 # 60% more than that
    more_guests_wife = john_guests * wife_more_percent

    # L2
    total_guests_wife = john_guests + more_guests_wife

    # L3
    cost_per_guest = 500 # cost $500 for each guest
    guests_total_cost = total_guests_wife * cost_per_guest

    # L4
    venue_cost = 10000 # The venue cost $10,000
    total_wedding_cost = guests_total_cost + venue_cost

    # FA
    answer = total_wedding_cost
    return answer