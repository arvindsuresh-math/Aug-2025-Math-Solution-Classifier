def solve():
    """Index: 1892.
    Returns: how many miles farther Tamika drove than Logan.
    """
    # L1
    tamika_hours = 8 # drove for 8 hours
    tamika_speed = 45 # average speed of 45 miles per hour
    tamika_miles = tamika_hours * tamika_speed

    # L2
    logan_hours = 5 # drove for 5 hours
    logan_speed = 55 # 55 miles an hour
    logan_miles = logan_hours * logan_speed

    # L3
    miles_farther = tamika_miles - logan_miles

    # FA
    answer = miles_farther
    return answer