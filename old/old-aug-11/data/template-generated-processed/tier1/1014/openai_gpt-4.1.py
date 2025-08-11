def solve():
    """Index: 1014.
    Returns: the total distance Hazel walked in 2 hours.
    """
    # L1
    first_hour_km = 2 # Hazel walked 2 kilometers in the first hour
    multiplier_second_hour = 2 # walked twice as far in the second hour
    second_hour_km = first_hour_km * multiplier_second_hour

    # L2
    total_km = first_hour_km + second_hour_km

    # FA
    answer = total_km
    return answer