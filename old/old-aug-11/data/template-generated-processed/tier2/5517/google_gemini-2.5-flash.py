def solve():
    """Index: 5517.
    Returns: how many minutes more Kwame and Connor studied than Lexia.
    """
    # L1
    kwame_study_hours = 2.5 # Kwame studied for the history test for 2.5 hours
    minutes_per_hour = 60 # WK
    kwame_study_minutes = kwame_study_hours * minutes_per_hour

    # L2
    connor_study_hours = 1.5 # Connor studied for 1.5 hours
    connor_study_minutes = connor_study_hours * minutes_per_hour

    # L3
    total_kwame_connor_minutes = kwame_study_minutes + connor_study_minutes

    # L4
    lexia_study_minutes = 97 # Lexia studied for 97 minutes
    difference_minutes = total_kwame_connor_minutes - lexia_study_minutes

    # FA
    answer = difference_minutes
    return answer