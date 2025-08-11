def solve():
    """Index: 4072.
    Returns: how many more calories the cake has than the brownies.
    """
    # L1
    cake_slices = 8 # 8 slices
    calories_per_cake_slice = 347 # each slice contains 347 calories
    total_cake_calories = cake_slices * calories_per_cake_slice

    # L2
    brownie_slices = 6 # 6 brownies
    calories_per_brownie_slice = 375 # each slice contains 375 calories
    total_brownie_calories = brownie_slices * calories_per_brownie_slice

    # L3
    calorie_difference = total_cake_calories - total_brownie_calories

    # FA
    answer = calorie_difference
    return answer