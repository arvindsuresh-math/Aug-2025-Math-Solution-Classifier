def solve():
    """Index: 7392.
    Returns: the total number of minutes Gina gets to choose.
    """
    # L4
    total_shows_watched_per_week = 24 # sister watches a total of 24 shows on Netflix per week
    coefficient_s = 4 # WK (derived from g=3s and g+s=24, leading to 4s=24)
    sister_shows_per_week = total_shows_watched_per_week / coefficient_s

    # L5
    gina_times_sister = 3 # Gina chooses what she and her sister will watch on Netflix three times as often as her sister does
    gina_shows_per_week = gina_times_sister * sister_shows_per_week

    # L6
    show_length_minutes = 50 # each show is 50 minutes long
    total_minutes_gina_chooses = gina_shows_per_week * show_length_minutes

    # FA
    answer = total_minutes_gina_chooses
    return answer