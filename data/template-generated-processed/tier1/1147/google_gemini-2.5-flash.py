def solve():
    """Index: 1147.
    Returns: the difference in the number of people between two cities with different cubic yard volumes.
    """
    # L1
    city_1_volume = 9000 # city with 9000 cubic yards
    city_2_volume = 6400 # city with 6400 cubic yards
    volume_difference = city_1_volume - city_2_volume

    # L2
    people_per_cubic_yard = 80 # number of people living per cubic yard is 80
    more_people = people_per_cubic_yard * volume_difference

    # FA
    answer = more_people
    return answer