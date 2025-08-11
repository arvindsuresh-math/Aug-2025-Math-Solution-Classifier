def solve():
    """Index: 1851.
    Returns: the total number of tomatoes Aubrey will have.
    """
    # L1
    total_rows = 15 # enough room for 15 rows of plants in total
    rows_per_tomato_plant_ratio = 3 # For each row of tomato plants, she is planting 2 rows of cucumbers (1 tomato + 2 cucumber = 3 rows per cycle)
    tomato_rows = total_rows / rows_per_tomato_plant_ratio

    # L2
    plants_per_row = 8 # enough space for 8 tomato plants in each row
    total_tomato_plants = tomato_rows * plants_per_row

    # L3
    tomatoes_per_plant = 3 # each plant produces 3 tomatoes
    total_tomatoes = total_tomato_plants * tomatoes_per_plant

    # FA
    answer = total_tomatoes
    return answer