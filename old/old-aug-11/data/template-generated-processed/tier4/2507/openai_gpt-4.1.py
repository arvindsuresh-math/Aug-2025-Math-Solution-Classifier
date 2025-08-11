def solve():
    """Index: 2507.
    Returns: the total distance of the relay race in miles.
    """
    # L1
    sadie_speed = 3 # Sadie: 3 miles per hour
    sadie_time = 2 # Sadie: 2 hours
    sadie_distance = sadie_speed * sadie_time

    # L2
    ariana_speed = 6 # Ariana: 6 miles per hour
    ariana_time = 0.5 # Ariana: half an hour
    ariana_distance = ariana_speed * ariana_time

    # L3
    total_time = 4.5 # total time for the race is four and half hours
    sarah_time = total_time - sadie_time - ariana_time

    # L4
    sarah_speed = 4 # Sarah: 4 miles per hour
    sarah_distance = sarah_speed * sarah_time

    # L5
    total_distance = sadie_distance + ariana_distance + sarah_distance

    # FA
    answer = total_distance
    return answer