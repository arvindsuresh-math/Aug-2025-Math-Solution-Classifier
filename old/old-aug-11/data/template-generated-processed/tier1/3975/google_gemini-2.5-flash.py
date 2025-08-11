def solve():
    """Index: 3975.
    Returns: the total miles Cheryl walked.
    """
    # L1
    miles_per_hour = 2 # walked 2 miles every hour
    hours_walked = 3 # for 3 hours
    distance_away = miles_per_hour * hours_walked

    # L2
    distance_back = distance_away # walked back home, another 6 miles
    total_miles_walked = distance_away + distance_back

    # FA
    answer = total_miles_walked
    return answer