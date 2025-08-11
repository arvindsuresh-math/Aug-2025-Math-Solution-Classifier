def solve():
    """Index: 3366.
    Returns: the difference in the amount of money Simon and Peter make in dollars.
    """
    # L1
    red_stamp_price_cents = 50 # 50 cents each
    num_red_stamps = 30 # 30 red stamps
    simon_cents = red_stamp_price_cents * num_red_stamps

    # L2
    white_stamp_price_cents = 20 # 20 cents each
    num_white_stamps = 80 # 80 white stamps
    peter_cents = white_stamp_price_cents * num_white_stamps

    # L3
    difference_in_cents = peter_cents - simon_cents

    # L4
    cents_per_dollar = 100 # WK
    difference_in_dollars = difference_in_cents / cents_per_dollar

    # FA
    answer = difference_in_dollars
    return answer