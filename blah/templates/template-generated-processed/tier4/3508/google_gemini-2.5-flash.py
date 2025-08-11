def solve():
    """Index: 3508.
    Returns: the average speed of his return journey.
    """
    # L1
    morning_speed = 30 # average speed of 30mph in the morning
    morning_time = 1 # 1 hr to drive to work in the morning
    distance_to_work = morning_speed * morning_time

    # L2
    evening_time = 1.5 # 1 and half hours to drive back home in the evening
    evening_speed = distance_to_work / evening_time

    # FA
    answer = evening_speed
    return answer