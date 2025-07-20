def solve():
    """Index: 5884.
    Returns: the number of badminton medals Jameson has.
    """
    # L1
    track_medals = 5 # Five of the medals are for the track
    swimming_multiplier = 2 # two times as many swimming medals
    swimming_medals = track_medals * swimming_multiplier

    # L2
    track_and_swimming_medals = track_medals + swimming_medals

    # L3
    total_medals = 20 # Jameson has 20 medals
    badminton_medals = total_medals - track_and_swimming_medals

    # FA
    answer = badminton_medals
    return answer