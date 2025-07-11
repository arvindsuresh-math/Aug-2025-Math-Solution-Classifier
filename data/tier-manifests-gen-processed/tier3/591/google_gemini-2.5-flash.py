def solve():
    """Index: 591.
    Returns: the total time in hours Veronica will take to pit all the cherries.
    """
    # L1
    cherries_per_pound = 80 # There are 80 single cherries in one pound of cherries
    pounds_needed = 3 # 3 pounds of pitted cherries
    total_cherries = cherries_per_pound * pounds_needed

    # L2
    cherries_per_unit = 20 # 20 cherries
    num_units = total_cherries / cherries_per_unit

    # L3
    minutes_per_unit = 10 # 10 minutes to pit 20 cherries
    total_minutes = minutes_per_unit * num_units

    # L4
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer