def solve():
    """Index: 6635.
    Returns: the number of apples Sarah gave to teachers.
    """
    # L1
    initial_apples = 25 # 25 apples
    friends_given = 5 # 5 of her closest friends
    apples_after_friends = initial_apples - friends_given

    # L2
    ate_walking_home = 1 # ate one of the apples
    apples_after_eating = apples_after_friends - ate_walking_home

    # L3
    apples_left_at_home = 3 # three apples left in the bag
    apples_given_to_teachers = apples_after_eating - apples_left_at_home

    # FA
    answer = apples_given_to_teachers
    return answer