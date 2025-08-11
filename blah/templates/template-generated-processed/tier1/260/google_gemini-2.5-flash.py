def solve():
    """Index: 260.
    Returns: the length of the shadows from the building in inches.
    """
    # L1
    shadow_increase_per_hour = 5 # Every hour past noon shadows from a building stretch an extra 5 feet
    hours_past_noon = 6 # 6 hours past noon
    shadow_length_feet = shadow_increase_per_hour * hours_past_noon

    # L2
    inches_per_foot = 12 # WK
    shadow_length_inches = shadow_length_feet * inches_per_foot

    # FA
    answer = shadow_length_inches
    return answer