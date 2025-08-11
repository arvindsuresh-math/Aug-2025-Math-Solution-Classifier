def solve():
    """Index: 3015.
    Returns: the amount of money Sam has left in cents.
    """
    # L1
    num_candy_bars = 4 # 4 candy bars
    cost_per_candy_bar_dimes = 3 # 3 dimes each
    cost_candy_bars_dimes = num_candy_bars * cost_per_candy_bar_dimes

    # L2
    initial_dimes = 19 # 19 dimes
    dimes_left = initial_dimes - cost_candy_bars_dimes

    # L3
    initial_quarters = 6 # 6 quarters
    quarters_for_lollipop = 1 # 1 lollipop for 1 quarter
    quarters_left = initial_quarters - quarters_for_lollipop

    # L4
    dime_value_cents = 10 # WK
    quarter_value_cents = 25 # WK
    total_cents_left = dimes_left * dime_value_cents + quarters_left * quarter_value_cents

    # FA
    answer = total_cents_left
    return answer