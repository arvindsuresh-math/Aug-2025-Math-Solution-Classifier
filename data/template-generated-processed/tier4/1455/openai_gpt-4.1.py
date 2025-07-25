from fractions import Fraction

def solve():
    """Index: 1455.
    Returns: the percentage of all plants that are tomato plants in both gardens.
    """
    # L1
    first_garden_plants = 20 # 20 plants in the first garden
    first_garden_tomato_fraction = 0.1 # 10% are tomato plants
    first_garden_tomatoes = first_garden_plants * first_garden_tomato_fraction

    # L2
    second_garden_plants = 15 # 15 plants in the second garden
    second_garden_tomato_fraction = Fraction(1, 3) # 1/3 of these plants are tomato plants
    second_garden_tomatoes = second_garden_plants * second_garden_tomato_fraction

    # L3
    total_tomatoes = first_garden_tomatoes + second_garden_tomatoes

    # L4
    total_plants = first_garden_plants + second_garden_plants

    # L5
    tomato_proportion = total_tomatoes / total_plants

    # L6
    percent_factor = 100 # WK
    tomato_percentage = tomato_proportion * percent_factor

    # FA
    answer = tomato_percentage
    return answer