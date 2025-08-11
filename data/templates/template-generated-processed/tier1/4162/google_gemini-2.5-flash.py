def solve():
    """Index: 4162.
    Returns: the total number of calories in Jerry's breakfast.
    """
    # L1
    num_pancakes = 6 # 6 pancakes
    calories_per_pancake = 120 # 120 calories each
    total_pancake_calories = num_pancakes * calories_per_pancake

    # L2
    num_bacon_strips = 2 # two strips of bacon
    calories_per_bacon_strip = 100 # 100 calories each
    total_bacon_calories = num_bacon_strips * calories_per_bacon_strip

    # L3
    calories_cereal = 200 # a bowl of cereal with 200 calories
    total_breakfast_calories = total_pancake_calories + total_bacon_calories + calories_cereal

    # FA
    answer = total_breakfast_calories
    return answer