def solve():
    """Index: 3496.
    Returns: the total number of pieces of tomatoes the farmer can get.
    """
    # L1
    num_rows = 30 # 30 rows of tomatoes
    plants_per_row = 10 # 10 plants in each row
    total_plants = num_rows * plants_per_row

    # L2
    yield_per_plant = 20 # 20 pieces of tomatoes
    total_tomatoes = total_plants * yield_per_plant

    # FA
    answer = total_tomatoes
    return answer