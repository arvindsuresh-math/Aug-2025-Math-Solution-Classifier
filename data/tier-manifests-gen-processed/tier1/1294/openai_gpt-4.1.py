def solve():
    """Index: 1294.
    Returns: the total number of hours Tom needs to get to the "Virgo" island.
    """
    # L1
    plane_multiplier = 4 # plane trip is four times longer
    boat_hours = 2 # boat trip takes up to 2 hours
    plane_hours = plane_multiplier * boat_hours

    # L2
    total_hours = plane_hours + boat_hours

    # FA
    answer = total_hours
    return answer