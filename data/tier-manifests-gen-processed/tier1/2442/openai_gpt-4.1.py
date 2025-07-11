def solve():
    """Index: 2442.
    Returns: the number of minutes Morgan can hula hoop.
    """
    # L1
    nancy_minutes = 10 # Nancy can hula hoop for 10 minutes
    casey_less_than_nancy = 3 # Casey can hula hoop 3 minutes less than Nancy
    casey_minutes = nancy_minutes - casey_less_than_nancy

    # L2
    morgan_times_casey = 3 # Morgan can hula hoop three times as long as Casey
    morgan_minutes = morgan_times_casey * casey_minutes

    # FA
    answer = morgan_minutes
    return answer