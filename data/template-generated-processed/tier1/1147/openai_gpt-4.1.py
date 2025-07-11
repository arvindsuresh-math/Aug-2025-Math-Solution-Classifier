def solve():
    """Index: 1147.
    Returns: how many more people are in a city with 9000 cubic yards than a city with 6400 cubic yards.
    """
    # L1
    cubic_yards_large = 9000 # city with 9000 cubic yards
    cubic_yards_small = 6400 # city with 6400 cubic yards
    difference_cubic_yards = cubic_yards_large - cubic_yards_small

    # L2
    people_per_cubic_yard = 80 # number of people living per cubic yard is 80
    more_people = people_per_cubic_yard * difference_cubic_yards

    # FA
    answer = more_people
    return answer