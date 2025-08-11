def solve():
    """Index: 5640.
    Returns: the additional money Phantom needs to buy all printer inks.
    """
    # L1
    num_black_inks = 2 # two black printer inks
    cost_black_ink = 11 # cost $11 each
    cost_black_inks = num_black_inks * cost_black_ink

    # L2
    num_red_inks = 3 # three red printer inks
    cost_red_ink = 15 # cost $15 each
    cost_red_inks = num_red_inks * cost_red_ink

    # L3
    num_yellow_inks = 2 # two yellow printer inks
    cost_yellow_ink = 13 # cost $13 each
    cost_yellow_inks = num_yellow_inks * cost_yellow_ink

    # L4
    total_cost_inks = cost_black_inks + cost_red_inks + cost_yellow_inks

    # L5
    money_given = 50 # gave him $50
    money_to_ask = total_cost_inks - money_given

    # FA
    answer = money_to_ask
    return answer