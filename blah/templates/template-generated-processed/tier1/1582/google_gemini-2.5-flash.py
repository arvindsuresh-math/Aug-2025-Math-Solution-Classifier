def solve():
    """Index: 1582.
    Returns: the total number of tickets Connie redeemed today.
    """
    # L1
    earbud_tickets = 10 # 10 tickets on a pair of earbuds
    glow_bracelet_tickets = 15 # another 15 tickets on glow bracelets
    earbuds_and_bracelets_tickets = earbud_tickets + glow_bracelet_tickets

    # L2
    koala_tickets = earbuds_and_bracelets_tickets # half of them on a stuffed koala bear

    # L3
    total_tickets_redeemed = earbuds_and_bracelets_tickets + koala_tickets

    # FA
    answer = total_tickets_redeemed
    return answer