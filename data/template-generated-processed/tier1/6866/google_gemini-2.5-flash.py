def solve():
    """Index: 6866.
    Returns: the difference between the number of geese and ducks remaining at the park.
    """
    # L1
    initial_ducks = 25 # 25 mallard ducks
    multiplier_twice = 2 # twice as many geese
    initial_geese_twice = initial_ducks * multiplier_twice

    # L2
    geese_less_than_twice = 10 # ten less than twice as many geese as ducks
    initial_geese = initial_geese_twice - geese_less_than_twice

    # L3
    arrived_ducks = 4 # 4 ducks arrived at the park
    total_ducks = initial_ducks + arrived_ducks

    # L4
    geese_initial_leaving_group = 15 # 15 geese
    geese_less_than_leaving_group = 5 # five less than 15 geese
    geese_leaving = geese_initial_leaving_group - geese_less_than_leaving_group

    # L5
    remaining_geese = initial_geese - geese_leaving

    # L6
    difference_geese_ducks = remaining_geese - total_ducks

    # FA
    answer = difference_geese_ducks
    return answer