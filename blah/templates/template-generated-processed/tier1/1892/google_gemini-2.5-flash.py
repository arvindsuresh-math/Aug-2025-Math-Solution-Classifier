def solve():
    """Index: 1892.
    Returns: how many miles farther Tamika drove.
    """
    # L1
    tamika_hours = 8 # 8 hours
    tamika_speed = 45 # 45 miles per hour
    tamika_distance = tamika_hours * tamika_speed

    # L2
    logan_hours = 5 # 5 hours
    logan_speed = 55 # 55 miles an hour
    logan_distance = logan_hours * logan_speed

    # L3
    difference_distance = tamika_distance - logan_distance

    # FA
    answer = difference_distance
    return answer