def solve():
    """Index: 5902.
    Returns: the total number of tomatoes produced by the three plants.
    """
    # L1
    first_plant_tomatoes = 24 # The first tomato plant produced two dozen tomatoes
    half_divisor = 2 # Half as many as the first plant
    half_first_plant_tomatoes = first_plant_tomatoes / half_divisor

    # L2
    additional_second_plant_tomatoes = 5 # 5 more than half as many tomatoes
    second_plant_tomatoes = half_first_plant_tomatoes + additional_second_plant_tomatoes

    # L3
    additional_third_plant_tomatoes = 2 # two more tomatoes than the second plant
    third_plant_tomatoes = second_plant_tomatoes + additional_third_plant_tomatoes

    # L4
    total_tomatoes = first_plant_tomatoes + second_plant_tomatoes + third_plant_tomatoes

    # FA
    answer = total_tomatoes
    return answer