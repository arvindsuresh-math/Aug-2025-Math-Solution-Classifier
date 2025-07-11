def solve():
    """Index: 2323.
    Returns: the number of thank you cards Jack needs.
    """
    # L1
    total_invitations = 200 # sent out 200 invitations
    rsvp_rate = 0.9 # 90% of people RSVPed
    num_rsvp = total_invitations * rsvp_rate

    # L2
    show_up_rate = 0.8 # 80% of people who RSVPed actually showed up
    num_showed_up = num_rsvp * show_up_rate

    # L3
    no_gift_attendees = 10 # 10 people who showed up didn't get a gift
    num_thank_you_cards = num_showed_up - no_gift_attendees

    # FA
    answer = num_thank_you_cards
    return answer