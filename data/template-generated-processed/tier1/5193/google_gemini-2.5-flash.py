def solve():
    """Index: 5193.
    Returns: the total number of plants remaining in Roxy's garden.
    """
    # L1
    initial_flowering_plants = 7 # 7 flowering plants

    # L2
    multiplier_fruiting = 2 # twice as many fruiting plants
    initial_fruiting_plants = initial_flowering_plants * multiplier_fruiting

    # L3
    bought_flowering_saturday = 3 # buys 3 flowering plants
    flowering_after_saturday = initial_flowering_plants + bought_flowering_saturday

    # L4
    bought_fruiting_saturday = 2 # buys 2 fruiting plants
    fruiting_after_saturday = initial_fruiting_plants + bought_fruiting_saturday

    # L5
    given_away_flowering_sunday = 1 # gives away 1 flowering plant
    flowering_after_sunday = flowering_after_saturday - given_away_flowering_sunday

    # L6
    given_away_fruiting_sunday = 4 # gives away 4 fruiting plants
    fruiting_after_sunday = fruiting_after_saturday - given_away_fruiting_sunday

    # L7
    total_remaining_plants = flowering_after_sunday + fruiting_after_sunday

    # FA
    answer = total_remaining_plants
    return answer