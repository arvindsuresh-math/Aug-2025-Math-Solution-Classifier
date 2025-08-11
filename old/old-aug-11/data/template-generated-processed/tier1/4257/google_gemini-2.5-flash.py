def solve():
    """Index: 4257.
    Returns: the total calories Dimitri gets after two days.
    """
    # L1
    calories_per_burger = 20 # 20 calories
    burgers_per_day = 3 # 3 burgers per day
    calories_per_day = calories_per_burger * burgers_per_day

    # L2
    num_days = 2 # two days
    total_calories = calories_per_day * num_days

    # FA
    answer = total_calories
    return answer