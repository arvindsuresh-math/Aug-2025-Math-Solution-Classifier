def solve():
    """Index: 2808.
    Returns: the time (in a.m.) Mark should leave his home to arrive at the same time as Rob.
    """
    # L1
    rob_time = 1 # It takes 1 hour for Rob to get to the national park
    mark_multiplier = 3 # three times as much time for Mark
    mark_time = rob_time * mark_multiplier

    # L2
    extra_time = mark_time - rob_time

    # L3
    rob_departure_time = 11 # Rob leaves his home at 11 a.m.
    mark_departure_time = rob_departure_time - extra_time

    # FA
    answer = mark_departure_time
    return answer