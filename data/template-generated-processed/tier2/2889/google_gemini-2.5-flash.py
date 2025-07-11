def solve():
    """Index: 2889.
    Returns: the number of guests who did not respond at all.
    """
    # L1
    total_guests = 200 # 200 guests
    yes_rsvp_percent_num = 83 # 83% of the guests
    percent_factor = 0.01 # WK
    yes_responses = total_guests * yes_rsvp_percent_num * percent_factor

    # L2
    no_rsvp_percent_num = 9 # 9% of the guests
    no_responses = total_guests * no_rsvp_percent_num * percent_factor

    # L3
    total_responded_guests = yes_responses + no_responses

    # L4
    unresponded_guests = total_guests - total_responded_guests

    # FA
    answer = unresponded_guests
    return answer