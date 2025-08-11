def solve():
    """Index: 4246.
    Returns: the total number of tomatoes Mabel has.
    """
    # L1
    first_plant_tomatoes = 8 # One tomato plant bore 8 tomatoes
    second_plant_more_than_first = 4 # another bore 4 more tomatoes than the first
    second_plant_tomatoes = first_plant_tomatoes + second_plant_more_than_first

    # L2
    first_two_combined = first_plant_tomatoes + second_plant_tomatoes

    # L3
    multiplier_for_remaining_plants = 3 # each bore three times the number of tomatoes
    remaining_plant_tomatoes = first_two_combined * multiplier_for_remaining_plants

    # L4
    total_tomatoes = first_plant_tomatoes + second_plant_tomatoes + remaining_plant_tomatoes + remaining_plant_tomatoes

    # FA
    answer = total_tomatoes
    return answer