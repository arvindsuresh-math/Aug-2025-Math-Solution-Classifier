def solve():
    """Index: 6177.
    Returns: the number of brownies left over.
    """
    # L1
    initial_total_brownies = 16 # cut them into 16 pieces
    children_eat_percent_decimal = 0.25 # ate 25% of the brownies
    children_eat_percent_text = 25 # ate 25% of the brownies
    percent_factor = 0.01 # WK
    children_eaten_brownies = children_eat_percent_text * percent_factor * initial_total_brownies

    # L2
    brownies_after_children = initial_total_brownies - children_eaten_brownies

    # L3
    family_eat_percent_decimal = 0.50 # ate 50% of the remaining brownies
    family_eat_percent_text = 50 # ate 50% of the remaining brownies
    family_eaten_brownies = family_eat_percent_text * percent_factor * brownies_after_children

    # L4
    brownies_after_family = brownies_after_children - family_eaten_brownies

    # L5
    lorraine_eats = 1 # Lorraine ate 1 more brownie
    brownies_left_over = brownies_after_family - lorraine_eats

    # FA
    answer = brownies_left_over
    return answer