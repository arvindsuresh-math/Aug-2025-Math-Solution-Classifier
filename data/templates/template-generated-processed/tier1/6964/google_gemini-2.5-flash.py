def solve():
    """Index: 6964.
    Returns: the number of excess calories James ate.
    """
    # L1
    ounces_per_bag = 2 # 2 ounces each
    num_bags = 3 # 3 bags
    total_ounces_eaten = ounces_per_bag * num_bags

    # L2
    calories_per_ounce = 150 # 150 calories in an ounce of Cheezits
    total_calories_eaten = total_ounces_eaten * calories_per_ounce

    # L3
    run_minutes = 40 # 40-minute run
    calories_burned_per_minute = 12 # burns 12 calories per minute
    total_calories_burned = run_minutes * calories_burned_per_minute

    # L4
    excess_calories = total_calories_eaten - total_calories_burned

    # FA
    answer = excess_calories
    return answer