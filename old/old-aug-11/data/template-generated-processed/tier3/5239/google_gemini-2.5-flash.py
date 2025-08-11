def solve():
    """Index: 5239.
    Returns: the length of time, in minutes, between eating each peanut.
    """
    # L1
    num_bags = 4 # four bags of peanuts
    peanuts_per_bag = 30 # Each bag contains 30 peanuts
    total_peanuts = num_bags * peanuts_per_bag

    # L2
    minutes_per_hour = 60 # WK
    flight_hours = 2 # 2-hour plane flight
    total_flight_minutes = minutes_per_hour * flight_hours

    # L3
    time_between_peanuts = total_flight_minutes / total_peanuts

    # FA
    answer = time_between_peanuts
    return answer