def solve():
    """Index: 4254.
    Returns: the degrees above the threshold of fever.
    """
    # L1
    normal_temperature = 95 # temperature of 95 degrees
    temperature_increase = 10 # raises his temperature by 10 degrees
    tony_current_temperature = normal_temperature + temperature_increase

    # L2
    fever_threshold = 100 # fever is anything over 100 degrees
    degrees_above_fever = tony_current_temperature - fever_threshold

    # FA
    answer = degrees_above_fever
    return answer