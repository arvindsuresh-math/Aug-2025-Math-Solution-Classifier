def solve():
    """Index: 1731.
    Returns: how much farther Margarita ran and jumped than Ricciana.
    """
    # L1
    ricciana_jump_distance = 4 # 4 feet for jumping
    multiplier_for_twice = 2 # twice Ricciana's jump
    twice_ricciana_jump = ricciana_jump_distance * multiplier_for_twice

    # L2
    less_than_twice_ricciana = 1 # 1 foot less than twice Ricciana's jump
    margarita_jump_distance = twice_ricciana_jump - less_than_twice_ricciana

    # L3
    margarita_run_distance = 18 # Margarita ran for 18 feet
    margarita_total_distance = margarita_run_distance + margarita_jump_distance

    # L4
    ricciana_total_distance = 24 # Ricciana ran and jumped a total of 24 feet
    difference_in_distance = margarita_total_distance - ricciana_total_distance

    # FA
    answer = difference_in_distance
    return answer