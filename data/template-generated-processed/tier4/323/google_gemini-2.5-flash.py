def solve():
    """Index: 323.
    Returns: the total amount spent at the craft store in dollars.
    """
    # L1
    jay_invited_guests = 22 # Jay invited 22 people
    gloria_invited_guests = 36 # Gloria invited 36
    total_guests_invited = jay_invited_guests + gloria_invited_guests

    # L2
    jay_own_flag = 1 # they also wanted 1 flag each
    gloria_own_flag = 1 # they also wanted 1 flag each
    total_flags_required = jay_own_flag + gloria_own_flag + total_guests_invited

    # L3
    flags_per_dollar_bundle = 5 # 5 flags for $1.00
    cost_per_dollar_bundle = 1.00 # $1.00
    total_cost_dollars = total_flags_required / flags_per_dollar_bundle

    # FA
    answer = total_cost_dollars
    return answer