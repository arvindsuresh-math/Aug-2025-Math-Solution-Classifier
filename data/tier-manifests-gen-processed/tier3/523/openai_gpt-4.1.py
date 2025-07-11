def solve():
    """Index: 523.
    Returns: the number of packs of detergent pods Hayes will need for a full year of laundry.
    """
    # L1
    pods_per_week = 3 # 3 loads of laundry a week using a detergent pod for each load
    weeks_per_year = 52 # 52 weeks in a year
    total_pods_needed = pods_per_week * weeks_per_year

    # L2
    pods_per_pack = 39 # detergent pods come 39 to a pack
    packs_needed = total_pods_needed / pods_per_pack

    # FA
    answer = packs_needed
    return answer