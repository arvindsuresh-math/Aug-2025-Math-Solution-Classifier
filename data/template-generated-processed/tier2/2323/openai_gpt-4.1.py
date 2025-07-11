def solve():
    """Index: 2323.
    Returns: the number of thank you cards Jack needs to send.
    """
    # L1
    invitations_sent = 200 # sent out 200 invitations
    rsvp_percent = 0.9 # 90% of people RSVPed
    num_rsvp = invitations_sent * rsvp_percent

    # L2
    show_up_percent = 0.8 # 80% of people who RSVPed actually showed up
    num_showed_up = num_rsvp * show_up_percent

    # L3
    no_gift = 10 # 10 people who showed up didn't get a gift
    num_thank_you_cards = num_showed_up - no_gift

    # FA
    answer = num_thank_you_cards
    return answer