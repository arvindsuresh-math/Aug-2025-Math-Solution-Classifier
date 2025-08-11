def solve():
    """Index: 7238.
    Returns: the weight of the first pack needed.
    """
    # L1
    hours_per_day = 8 # 8 hours a day
    num_days = 5 # for 5 days
    total_hiking_hours = hours_per_day * num_days

    # L2
    hiking_rate_mph = 2.5 # hike at a rate of 2.5 mph
    total_miles = total_hiking_hours * hiking_rate_mph

    # L3
    supplies_per_mile = 0.5 # pack about .5 pounds of supplies for every mile
    total_supplies_needed = total_miles * supplies_per_mile

    # L4
    base_pack_factor = 1 # WK
    resupply_percentage = 0.25 # 25% as large as his first pack
    total_pack_multiplier = base_pack_factor + resupply_percentage

    # L5
    initial_pack_weight = total_supplies_needed / total_pack_multiplier

    # FA
    answer = initial_pack_weight
    return answer