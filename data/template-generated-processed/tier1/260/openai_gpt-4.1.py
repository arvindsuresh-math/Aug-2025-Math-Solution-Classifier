def solve():
    """Index: 260.
    Returns: the length of the building's shadow in inches 6 hours past noon.
    """
    # L1
    feet_per_hour = 5 # shadows stretch an extra 5 feet every hour past noon
    hours_past_noon = 6 # 6 hours past noon
    shadow_length_feet = feet_per_hour * hours_past_noon

    # L2
    inches_per_foot = 12 # WK
    shadow_length_inches = shadow_length_feet * inches_per_foot

    # FA
    answer = shadow_length_inches
    return answer