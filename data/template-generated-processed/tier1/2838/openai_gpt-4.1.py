def solve():
    """Index: 2838.
    Returns: the total number of feet the friends walked combined.
    """
    # L1
    lionel_miles = 4 # Lionel walked 4 miles
    feet_per_mile = 5280 # WK
    lionel_feet = lionel_miles * feet_per_mile

    # L2
    esther_yards = 975 # Esther walked 975 yards
    feet_per_yard = 3 # WK
    esther_feet = esther_yards * feet_per_yard

    # L3
    niklaus_feet = 1287 # Niklaus walked 1287 feet
    total_feet = lionel_feet + esther_feet + niklaus_feet

    # FA
    answer = total_feet
    return answer