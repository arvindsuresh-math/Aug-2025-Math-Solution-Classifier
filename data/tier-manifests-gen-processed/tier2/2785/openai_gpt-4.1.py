def solve():
    """Index: 2785.
    Returns: the total wedding cost if John's wife gets her way.
    """
    # L1
    john_guests = 50 # John wants 50 guests
    wife_extra_percent = 0.6 # wife wants 60% more than that
    wife_extra_guests = john_guests * wife_extra_percent

    # L2
    wife_guests = john_guests + wife_extra_guests

    # L3
    cost_per_guest = 500 # $500 for each guest
    guests_cost = wife_guests * cost_per_guest

    # L4
    venue_cost = 10000 # venue cost $10,000
    total_cost = guests_cost + venue_cost

    # FA
    answer = total_cost
    return answer