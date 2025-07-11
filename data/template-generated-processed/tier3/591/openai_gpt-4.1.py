def solve():
    """Index: 591.
    Returns: the number of hours it will take Veronica to pit all the cherries.
    """
    # L1
    cherries_per_pound = 80 # 80 single cherries in one pound of cherries
    pounds_needed = 3 # needs 3 pounds to make a pie
    total_cherries = cherries_per_pound * pounds_needed

    # L2
    cherries_per_unit = 20 # pit 20 cherries per unit
    total_units = total_cherries / cherries_per_unit

    # L3
    minutes_per_unit = 10 # 10 minutes to pit a unit
    total_minutes = minutes_per_unit * total_units

    # L4
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer