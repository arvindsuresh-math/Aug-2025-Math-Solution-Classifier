def solve():
    """Index: 810.
    Returns: the total number of CDs Tyler has now.
    """
    # L1
    initial_cds = 21 # Tyler has 21 CDs
    fraction_given_away_denominator = 3 # a third of his CDs
    cds_given_away = initial_cds / fraction_given_away_denominator

    # L2
    cds_after_giving_away = initial_cds - cds_given_away

    # L3
    new_cds_bought = 8 # buys 8 brand new CDs
    total_cds_now = cds_after_giving_away + new_cds_bought

    # FA
    answer = total_cds_now
    return answer