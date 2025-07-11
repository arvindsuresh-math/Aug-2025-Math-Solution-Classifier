def solve():
    """Index: 331.
    Returns: the number of barrels of pitch needed to finish the remaining road on the third day.
    """
    # L1
    first_day_miles = 4 # paved 4 miles of road on one day
    second_day_multiplier = 2 # double that
    second_day_subtract = 1 # one mile less than double
    second_day_miles = first_day_miles * second_day_multiplier - second_day_subtract

    # L2
    total_miles = 16 # newly constructed 16-mile road
    remaining_miles = total_miles - second_day_miles - first_day_miles

    # L3
    truckloads_per_mile = 3 # three truckloads of asphalt to pave each mile
    needed_truckloads = truckloads_per_mile * remaining_miles

    # L4
    bags_gravel_per_truckload = 2 # two bags of gravel per truckload
    total_bags_gravel = needed_truckloads * bags_gravel_per_truckload

    # L5
    gravel_per_pitch_ratio = 5 # five times as many bags of gravel as barrels of pitch
    barrels_pitch = total_bags_gravel / gravel_per_pitch_ratio

    # FA
    answer = barrels_pitch
    return answer