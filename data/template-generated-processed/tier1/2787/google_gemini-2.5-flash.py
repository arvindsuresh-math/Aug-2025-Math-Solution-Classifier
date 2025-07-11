def solve():
    """Index: 2787.
    Returns: the total ounces of water Remi drinks in 7 days.
    """
    # L1
    bottle_capacity = 20 # holds 20 ounces of water
    refills_per_day = 3 # refills the bottle 3 times a day
    daily_intake_no_spill = bottle_capacity * refills_per_day

    # L2
    num_days_in_week = 7 # In 7 days
    total_intake_no_spill = daily_intake_no_spill * num_days_in_week

    # L3
    spill_1 = 5 # spills 5 ounces the first time
    spill_2 = 8 # spills 8 ounces the second time
    total_spilled_water = spill_2 + spill_1

    # L4
    actual_intake = total_intake_no_spill - total_spilled_water

    # FA
    answer = actual_intake
    return answer