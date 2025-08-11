def solve():
    """Index: 3801.
    Returns: the total number of animals in Savanna National park.
    """
    # L1
    safari_lions = 100 # 100 lions
    snake_fraction_numerator = 1 # half as many snakes
    snake_fraction_denominator = 2 # half as many snakes
    safari_snakes = snake_fraction_numerator / snake_fraction_denominator * safari_lions

    # L2
    giraffes_fewer_than_snakes = 10 # 10 fewer giraffes than snakes
    safari_giraffes = safari_snakes - giraffes_fewer_than_snakes

    # L3
    savanna_lion_multiplier = 2 # double as many lions
    savanna_lions = safari_lions * savanna_lion_multiplier

    # L4
    savanna_snake_multiplier = 3 # triple as many snakes
    savanna_snakes = safari_snakes * savanna_snake_multiplier

    # L5
    savanna_giraffe_increase = 20 # 20 more giraffes
    savanna_giraffes = safari_giraffes + savanna_giraffe_increase

    # L6
    total_savanna_animals = savanna_lions + savanna_snakes + savanna_giraffes

    # FA
    answer = total_savanna_animals
    return answer