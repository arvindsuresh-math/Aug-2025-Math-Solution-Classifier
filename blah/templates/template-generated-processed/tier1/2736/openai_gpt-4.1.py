def solve():
    """Index: 2736.
    Returns: the total vertical feet Paul travels over the week.
    """
    # L1
    trips_per_day = 3 # makes 3 trips out from and back to his apartment throughout the day
    up_and_down_per_trip = 2 # each trip involves going both down and up
    trips_per_day_total = trips_per_day * up_and_down_per_trip

    # L2
    days_in_week = 7 # WK
    trips_per_week = trips_per_day_total * days_in_week

    # L3
    stories = 5 # 5th story apartment
    feet_per_story = 10 # each story is 10 feet tall
    feet_per_trip = stories * feet_per_story

    # L4
    total_feet = feet_per_trip * trips_per_week

    # FA
    answer = total_feet
    return answer