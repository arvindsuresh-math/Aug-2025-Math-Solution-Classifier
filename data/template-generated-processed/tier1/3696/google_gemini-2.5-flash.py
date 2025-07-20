def solve():
    """Index: 3696.
    Returns: the total kilometers Christina covered that week.
    """
    # L1
    distance_to_school = 7 # 7km to school
    round_trip_multiplier = 2 # returns home covering the same distance
    distance_per_day = round_trip_multiplier * distance_to_school

    # L2
    school_days_per_week = 5 # every day from Monday to Friday
    distance_to_school_per_week = distance_per_day * school_days_per_week

    # L3
    extra_distance_to_friend = 2 # another 2km away from the school
    round_trip_multiplier_friend = 2 # WK
    extra_distance_total = extra_distance_to_friend * round_trip_multiplier_friend

    # L4
    total_distance_week = distance_to_school_per_week + extra_distance_total

    # FA
    answer = total_distance_week
    return answer