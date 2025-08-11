def solve():
    """Index: 1582.
    Returns: the total number of tickets Connie redeemed today.
    """
    # L1
    earbuds_tickets = 10 # 10 tickets on a pair of earbuds
    glow_bracelets_tickets = 15 # 15 tickets on glow bracelets
    other_half_tickets = earbuds_tickets + glow_bracelets_tickets

    # L2
    koala_half_tickets = other_half_tickets # half spent on koala bear equals other half

    # L3
    total_tickets = other_half_tickets + koala_half_tickets

    # FA
    answer = total_tickets
    return answer