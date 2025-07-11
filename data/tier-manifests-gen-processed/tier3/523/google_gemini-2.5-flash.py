def solve():
    """Index: 523.
    Returns: the number of detergent packs needed for a year.
    """
    # L1
    pods_per_week = 3 # 3 loads of laundry a week using a detergent pod for each load
    weeks_per_year = 52 # WK
    total_pods_needed_per_year = pods_per_week * weeks_per_year

    # L2
    pods_per_pack = 39 # His detergent pods come 39 to a pack
    packs_needed = total_pods_needed_per_year / pods_per_pack

    # FA
    answer = packs_needed
    return answer