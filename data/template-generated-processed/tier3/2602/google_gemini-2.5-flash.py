def solve():
    """Index: 2602.
    Returns: the number of cookies each kid gets.
    """
    # L1
    calories_per_carrot = 20 # 20 calories each
    num_carrot_sticks = 5 # 5 carrot sticks
    total_carrot_calories = calories_per_carrot * num_carrot_sticks

    # L2
    goal_calories = 750 # total of 750 calories
    burger_calories = 400 # burger with 400 calories
    remaining_calories = goal_calories - burger_calories - total_carrot_calories

    # L3
    calories_per_cookie = 50 # 50 calories each
    num_cookies = remaining_calories / calories_per_cookie

    # FA
    answer = num_cookies
    return answer