def solve():
    """Index: 2889.
    Returns: the number of guests who did not respond at all.
    """
    # L1
    total_guests = 200 # 200 guests
    yes_percent_num = 83 # 83% of the guests RSVP with a Yes response
    percent_factor = 0.01 # WK
    yes_rsvp = total_guests * yes_percent_num * percent_factor

    # L2
    no_percent_num = 9 # 9% of the guests RSVP with a No response
    no_rsvp = total_guests * no_percent_num * percent_factor

    # L3
    responded_guests = yes_rsvp + no_rsvp

    # L4
    non_responded_guests = total_guests - responded_guests

    # FA
    answer = non_responded_guests
    return answer