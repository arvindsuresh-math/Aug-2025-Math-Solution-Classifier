def solve():
    """Index: 3320.
    Returns: how many more vegetables Pauline could plant in her garden.
    """
    # L1
    num_tomato_kinds = 3 # 3 kinds of tomatoes
    tomatoes_per_kind = 5 # 5 of each kind
    total_tomatoes = num_tomato_kinds * tomatoes_per_kind

    # L2
    num_cucumber_kinds = 5 # 5 kinds of cucumbers
    cucumbers_per_kind = 4 # 4 of each kind
    total_cucumbers = num_cucumber_kinds * cucumbers_per_kind

    # L3
    num_potatoes = 30 # 30 potatoes
    total_planted_vegetables = total_tomatoes + total_cucumbers + num_potatoes

    # L4
    num_rows = 10 # 10 rows
    spaces_per_row = 15 # 15 spaces in each
    garden_capacity = num_rows * spaces_per_row

    # L5
    more_vegetables_to_plant = garden_capacity - total_planted_vegetables

    # FA
    answer = more_vegetables_to_plant
    return answer