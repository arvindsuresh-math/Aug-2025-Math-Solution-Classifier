def solve():
    """Index: 6949.
    Returns: the total number of calories John ate.
    """
    # L1
    total_chip_calories = 60 # 60 calories
    num_chips = 10 # 10 potato chips
    calories_per_chip = total_chip_calories / num_chips

    # L2
    cheezit_calorie_fraction_denominator = 3 # 1/3 more calories
    additional_calories_per_cheezit = calories_per_chip / cheezit_calorie_fraction_denominator

    # L3
    calories_per_cheezit = calories_per_chip + additional_calories_per_cheezit

    # L4
    num_cheezits = 6 # 6 cheezits
    total_cheezit_calories = num_cheezits * calories_per_cheezit

    # L5
    total_calories_eaten = total_chip_calories + total_cheezit_calories

    # FA
    answer = total_calories_eaten
    return answer