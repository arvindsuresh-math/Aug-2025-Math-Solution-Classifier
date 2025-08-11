def solve():
    """Index: 1602.
    Returns: the number of kilometers Amelia still has to drive to make it across the country.
    """
    # L1
    monday_km = 907 # drove 907 kilometers on Monday
    tuesday_km = 582 # 582 kilometers on Tuesday
    distance_driven = monday_km + tuesday_km

    # L2
    total_distance = 8205 # The distance across a country is 8205 kilometers
    distance_remaining = total_distance - distance_driven

    # FA
    answer = distance_remaining
    return answer