def solve():
    """Index: 4878.
    Returns: the number of plants remaining in the garden.
    """
    # L1
    initial_plants = 30 # garden of 30 plants
    first_eaten_plants = 20 # completely ate 20 plants
    plants_after_first_eat = initial_plants - first_eaten_plants

    # L2
    half_divisor = 2 # only ate half of the remaining plants
    plants_after_second_eat = plants_after_first_eat / half_divisor

    # L3
    third_eaten_plants = 1 # only ate 1 of the plants that were left
    remaining_plants = plants_after_second_eat - third_eaten_plants

    # FA
    answer = remaining_plants
    return answer