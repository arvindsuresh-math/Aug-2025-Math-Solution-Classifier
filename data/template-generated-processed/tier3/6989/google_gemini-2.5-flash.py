def solve():
    """Index: 6989.
    Returns: the total number of paintings the artist can make in four weeks.
    """
    # L1
    painting_hours_per_week = 30 # An artist spends 30 hours every week painting
    hours_per_painting = 3 # it takes her 3 hours to complete a painting
    paintings_per_week = painting_hours_per_week / hours_per_painting

    # L2
    weeks_in_period = 4 # in four weeks
    total_paintings = paintings_per_week * weeks_in_period

    # FA
    answer = total_paintings
    return answer