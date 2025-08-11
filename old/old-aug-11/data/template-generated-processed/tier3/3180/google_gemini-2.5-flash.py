def solve():
    """Index: 3180.
    Returns: the number of servings of peanut butter Toby should add.
    """
    # L1
    total_desired_calories = 500 # 500 calories for breakfast
    calories_per_bread_piece = 100 # A piece of bread has 100 calories
    calories_needed_from_pb = total_desired_calories - calories_per_bread_piece

    # L2
    calories_per_pb_serving = 200 # A serving of peanut butter has 200 calories
    servings_of_pb = calories_needed_from_pb / calories_per_pb_serving

    # FA
    answer = servings_of_pb
    return answer