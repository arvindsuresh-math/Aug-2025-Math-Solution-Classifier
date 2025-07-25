def solve():
    """Index: 4968.
    Returns: the total number of calories Tom ate.
    """
    # L1
    broccoli_multiplier = 2 # twice as much broccoli
    carrots_pounds = 1 # a pound of carrots
    broccoli_pounds = broccoli_multiplier * carrots_pounds

    # L2
    carrots_calories_per_pound = 51 # carrots have 51 calories per pound
    broccoli_calorie_divisor = 3 # broccoli has 1/3 that many calories
    broccoli_calories_per_pound = carrots_calories_per_pound / broccoli_calorie_divisor

    # L3
    total_broccoli_calories = broccoli_pounds * broccoli_calories_per_pound

    # L4
    total_carrots_calories = carrots_pounds * carrots_calories_per_pound

    # L5
    total_calories_eaten = total_carrots_calories + total_broccoli_calories

    # FA
    answer = total_calories_eaten
    return answer