def solve():
    """Index: 2808.
    Returns: the time Mark should leave his home.
    """
    # L1
    rob_travel_time_hours = 1 # 1 hour for Rob to get to the national park
    mark_time_multiplier = 3 # three times as much time for Mark
    mark_travel_time_hours = rob_travel_time_hours * mark_time_multiplier

    # L2
    extra_time_mark_takes_hours = mark_travel_time_hours - rob_travel_time_hours

    # L3
    rob_departure_hour = 11 # Rob leaves his home at 11 a.m.
    mark_departure_hour = rob_departure_hour - extra_time_mark_takes_hours

    # FA
    answer = mark_departure_hour
    return answer