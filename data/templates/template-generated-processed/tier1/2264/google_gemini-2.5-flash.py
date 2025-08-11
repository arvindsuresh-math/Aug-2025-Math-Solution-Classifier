def solve():
    """Index: 2264.
    Returns: the number of people living in Sun City.
    """
    # L1
    multiplier_thrice = 3 # thrice as many people
    willowdale_people = 2000 # Willowdale city has 2000 people
    less_than_thrice = 500 # 500 less than thrice as many people
    roseville_people = multiplier_thrice * willowdale_people - less_than_thrice

    # L2
    multiplier_twice = 2 # twice as many people
    more_than_twice = 1000 # 1000 more than twice as many people
    sun_city_people = multiplier_twice * roseville_people + more_than_twice

    # FA
    answer = sun_city_people
    return answer