def solve():
    """Index: 6894.
    Returns: the percentage of the sandwich's total calories that come from bacon.
    """
    # L1
    calories_per_bacon_strip = 125 # 125 calories each
    total_bacon_calories = calories_per_bacon_strip + calories_per_bacon_strip

    # L2
    total_sandwich_calories = 1250 # 1250 calories total
    percentage_multiplier = 100 # 100%
    bacon_percentage = (total_bacon_calories / total_sandwich_calories) * percentage_multiplier

    # FA
    answer = bacon_percentage
    return answer