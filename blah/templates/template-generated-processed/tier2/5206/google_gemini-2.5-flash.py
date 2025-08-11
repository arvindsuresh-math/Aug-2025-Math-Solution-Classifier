def solve():
    """Index: 5206.
    Returns: the height of the cow manure plant in inches.
    """
    # L1
    control_plant_height = 36 # grows 36 inches high
    bone_meal_percent_num = 125 # 125% of the height
    percent_factor = 0.01 # WK
    bone_meal_plant_height = control_plant_height * bone_meal_percent_num * percent_factor

    # L2
    cow_manure_percent_num = 200 # 200% of the height
    cow_manure_plant_height = bone_meal_plant_height * cow_manure_percent_num * percent_factor

    # FA
    answer = cow_manure_plant_height
    return answer