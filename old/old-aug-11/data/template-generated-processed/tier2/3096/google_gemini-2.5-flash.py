def solve():
    """Index: 3096.
    Returns: the temperature at 11 A.M..
    """
    # L1
    initial_temperature = 50 # temperature was 50 degrees at 3 A.M.
    temp_increase_per_interval = 1.5 # went up 1.5 degrees every 2 hours
    temp_at_5am = initial_temperature + temp_increase_per_interval

    # L2
    temp_at_7am = temp_at_5am + temp_increase_per_interval

    # L3
    temp_at_9am = temp_at_7am + temp_increase_per_interval

    # L4
    temp_at_11am = temp_at_9am + temp_increase_per_interval

    # FA
    answer = temp_at_11am
    return answer