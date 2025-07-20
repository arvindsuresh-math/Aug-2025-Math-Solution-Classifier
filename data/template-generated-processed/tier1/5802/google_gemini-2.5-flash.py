def solve():
    """Index: 5802.
    Returns: the number of meters farther Hannah ran on Monday than Wednesday and Friday combined.
    """
    # L1
    wednesday_distance = 4816 # 4816 meters on Wednesday
    friday_distance = 2095 # 2095 meters on Friday
    wednesday_friday_combined = wednesday_distance + friday_distance

    # L2
    monday_distance_km = 9 # 9 kilometers on Monday
    meters_per_km = 1000 # WK
    monday_distance_meters = monday_distance_km * meters_per_km

    # L3
    difference_meters = monday_distance_meters - wednesday_friday_combined

    # FA
    answer = difference_meters
    return answer