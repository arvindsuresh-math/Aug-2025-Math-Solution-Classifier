def solve():
    """Index: 3435.
    Returns: the difference in calories per dollar between burgers and burritos.
    """
    # L1
    num_burritos = 10 # 10 burritos
    calories_per_burrito = 120 # 120 calories each
    total_burrito_calories = num_burritos * calories_per_burrito

    # L2
    cost_burritos = 6 # $6
    burrito_calories_per_dollar = total_burrito_calories / cost_burritos

    # L3
    num_burgers = 5 # 5 burgers
    calories_per_burger = 400 # 400 calories each
    total_burger_calories = num_burgers * calories_per_burger

    # L4
    cost_burgers = 8 # $8
    burger_calories_per_dollar = total_burger_calories / cost_burgers

    # L5
    calories_per_dollar_difference = burger_calories_per_dollar - burrito_calories_per_dollar

    # FA
    answer = calories_per_dollar_difference
    return answer