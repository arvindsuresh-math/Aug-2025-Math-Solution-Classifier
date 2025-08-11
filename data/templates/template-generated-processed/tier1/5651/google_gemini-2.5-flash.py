def solve():
    """Index: 5651.
    Returns: the total number of bananas Nathan had.
    """
    # L1
    num_bunches_eight = 6 # six bunches
    bananas_per_bunch_eight = 8 # eight bananas in a bunch
    bananas_from_eight_bunches = num_bunches_eight * bananas_per_bunch_eight

    # L2
    num_bunches_seven = 5 # five bunches
    bananas_per_bunch_seven = 7 # seven bananas in a bunch
    bananas_from_seven_bunches = num_bunches_seven * bananas_per_bunch_seven

    # L3
    total_bananas = bananas_from_eight_bunches + bananas_from_seven_bunches

    # FA
    answer = total_bananas
    return answer