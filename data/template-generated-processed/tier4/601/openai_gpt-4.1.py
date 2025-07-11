def solve():
    """Index: 601.
    Returns: the number of seconds it takes for the cheetah to catch the gazelle.
    """
    # L1
    cheetah_speed_mph = 60 # A cheetah can run at a top speed of 60 mph
    mph_to_fps = 1.5 # one mile per hour is about 1.5 feet per second
    cheetah_speed_fps = cheetah_speed_mph * mph_to_fps

    # L2
    gazelle_speed_mph = 40 # The gazelle can run for speeds of up to 40 miles per hour
    gazelle_speed_fps = gazelle_speed_mph * mph_to_fps

    # L3
    relative_speed_fps = cheetah_speed_fps - gazelle_speed_fps

    # L4
    initial_distance = 210 # they were initially 210 feet apart
    time_to_catch = initial_distance / relative_speed_fps

    # FA
    answer = time_to_catch
    return answer