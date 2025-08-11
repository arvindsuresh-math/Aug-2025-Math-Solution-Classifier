def solve():
    """Index: 5280.
    Returns: the total number of eggs sold that day.
    """
    # L1
    collected_trays = 10 # collect 10 trays of eggs
    dropped_trays = 2 # dropped two trays
    remaining_trays_after_drop = collected_trays - dropped_trays

    # L2
    added_trays = 7 # add 7 more trays
    total_trays = remaining_trays_after_drop + added_trays

    # L3
    eggs_per_tray = 36 # WK
    total_eggs_sold = eggs_per_tray * total_trays

    # FA
    answer = total_eggs_sold
    return answer