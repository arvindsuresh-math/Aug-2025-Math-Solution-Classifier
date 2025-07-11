def solve():
    """Index: 331.
    Returns: the number of barrels of pitch the company will need to finish the remaining road.
    """
    # L1
    miles_paved_day1 = 4 # paved 4 miles of road on one day
    double_multiplier = 2 # double that
    miles_less = 1 # one mile less
    miles_paved_day2 = miles_paved_day1 * double_multiplier - miles_less

    # L2
    total_road_miles = 16 # newly constructed 16-mile road
    remaining_miles = total_road_miles - miles_paved_day2 - miles_paved_day1

    # L3
    truckloads_per_mile = 3 # It takes three truckloads of asphalt to pave each mile of road
    truckloads_needed = truckloads_per_mile * remaining_miles

    # L4
    gravel_per_truckload = 2 # uses two bags of gravel
    gravel_bags_needed = truckloads_needed * gravel_per_truckload

    # L5
    gravel_to_pitch_ratio = 5 # five times as many bags of gravel as it does barrels of pitch
    pitch_barrels_needed = gravel_bags_needed / gravel_to_pitch_ratio

    # FA
    answer = pitch_barrels_needed
    return answer