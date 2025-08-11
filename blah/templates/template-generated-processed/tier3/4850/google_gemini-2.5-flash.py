def solve():
    """Index: 4850.
    Returns: the percentage more birds Gabrielle saw than Chase.
    """
    # L1
    gabrielle_robins = 5 # Gabrielle saw 5 robins
    gabrielle_cardinals = 4 # 4 cardinals
    gabrielle_blue_jays = 3 # and 3 blue jays
    total_gabrielle_birds = gabrielle_robins + gabrielle_cardinals + gabrielle_blue_jays

    # L2
    chase_robins = 2 # Chase saw 2 robins
    chase_blue_jays = 3 # 3 blue jays
    chase_cardinals = 5 # and 5 cardinals
    total_chase_birds = chase_robins + chase_blue_jays + chase_cardinals

    # L3
    difference_in_birds = total_gabrielle_birds - total_chase_birds

    # L4
    percentage_multiplier = 100 # x 100%
    percentage_more = (difference_in_birds / total_chase_birds) * percentage_multiplier

    # FA
    answer = percentage_more
    return answer