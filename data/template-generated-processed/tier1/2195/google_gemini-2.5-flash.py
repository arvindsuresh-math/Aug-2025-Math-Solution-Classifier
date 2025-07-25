def solve():
    """Index: 2195.
    Returns: the total distance Shane drives in an 80-day semester.
    """
    # L1
    miles_one_way = 10 # 10 miles
    round_trip_multiplier = 2 # WK
    miles_per_day = round_trip_multiplier * miles_one_way

    # L2
    semester_days = 80 # 80 day semester
    total_distance = semester_days * miles_per_day

    # FA
    answer = total_distance
    return answer