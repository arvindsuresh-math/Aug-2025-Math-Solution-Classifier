def solve():
    """Index: 6595.
    Returns: Jacob's current age.
    """
    # L1
    john_age = 30 # John is 30
    maya_age_divisor = 2 # twice as old as Maya
    maya_age = john_age / maya_age_divisor

    # L2
    drew_age_difference = 5 # Drew is 5 years older than Maya
    drew_age = maya_age + drew_age_difference

    # L3
    peter_age_difference = 4 # Peter is 4 years older than Drew
    peter_age = drew_age + peter_age_difference

    # L4
    years_in_future = 2 # In 2 years
    peter_age_in_2_years = peter_age + years_in_future

    # L5
    jacob_age_divisor = 2 # exactly half of Peter’s age
    jacob_age_in_2_years = peter_age_in_2_years / jacob_age_divisor

    # L6
    jacob_current_age = jacob_age_in_2_years - years_in_future

    # FA
    answer = jacob_current_age
    return answer