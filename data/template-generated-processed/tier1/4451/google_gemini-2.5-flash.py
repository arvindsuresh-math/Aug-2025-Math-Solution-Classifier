def solve():
    """Index: 4451.
    Returns: the number of m&m's Cheryl gave to her sister.
    """
    # L1
    eaten_after_lunch = 7 # ate 7 m&m's after lunch
    eaten_after_dinner = 5 # ate 5 m&m's after dinner
    total_eaten_by_cheryl = eaten_after_lunch + eaten_after_dinner

    # L2
    initial_mms = 25 # had 25 m&m's at the beginning
    given_to_sister = initial_mms - total_eaten_by_cheryl

    # FA
    answer = given_to_sister
    return answer