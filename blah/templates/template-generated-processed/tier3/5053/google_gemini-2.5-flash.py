def solve():
    """Index: 5053.
    Returns: the total number of colors the sky turned.
    """
    # L1
    duration_hours = 2 # two hours
    minutes_per_hour = 60 # sixty minutes long
    total_minutes = duration_hours * minutes_per_hour

    # L2
    time_per_color_change = 10 # Every ten minutes
    number_of_colors = total_minutes / time_per_color_change

    # FA
    answer = number_of_colors
    return answer