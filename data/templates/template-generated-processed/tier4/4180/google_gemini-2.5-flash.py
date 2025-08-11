def solve():
    """Index: 4180.
    Returns: the total amount Maria will spend on soap for the entire year.
    """
    # L1
    months_per_bar = 2 # lasts her for 2 months
    months_per_year = 12 # WK
    num_bars_needed = months_per_year / months_per_bar

    # L2
    cost_per_bar = 8.00 # $8.00 per bar of soap
    total_cost = cost_per_bar * num_bars_needed

    # FA
    answer = total_cost
    return answer