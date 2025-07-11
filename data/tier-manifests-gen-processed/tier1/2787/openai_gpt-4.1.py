def solve():
    """Index: 2787.
    Returns: the total ounces of water Remi drinks in 7 days accounting for spills.
    """
    # L1
    bottle_ounces = 20 # holds 20 ounces of water
    refills_per_day = 3 # refills the bottle 3 times a day
    daily_ounces = bottle_ounces * refills_per_day

    # L2
    days = 7 # In 7 days
    total_ounces_no_spill = daily_ounces * days

    # L3
    spill1 = 5 # spills 5 ounces the first time
    spill2 = 8 # spills 8 ounces the second time
    total_spilled = spill2 + spill1

    # L4
    total_ounces = total_ounces_no_spill - total_spilled

    # FA
    answer = total_ounces
    return answer