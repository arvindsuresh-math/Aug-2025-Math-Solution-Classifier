def solve():
    """Index: 3909.
    Returns: the net amount of money John spent.
    """
    # L1
    acts_per_play = 5 # Each play has 5 Acts
    wigs_per_act = 2 # He wears 2 wigs per act
    wigs_per_play = acts_per_play * wigs_per_act

    # L2
    num_plays = 3 # John is performing in 3 plays
    total_wigs_initial = wigs_per_play * num_plays

    # L3
    cost_per_wig = 5 # Each wig cost $5
    total_cost_initial = total_wigs_initial * cost_per_wig

    # L4
    sale_price_per_wig = 4 # sells all of the wigs for that play for $4
    money_back_from_sale = wigs_per_play * sale_price_per_wig

    # L5
    net_spent = total_cost_initial - money_back_from_sale

    # FA
    answer = net_spent
    return answer