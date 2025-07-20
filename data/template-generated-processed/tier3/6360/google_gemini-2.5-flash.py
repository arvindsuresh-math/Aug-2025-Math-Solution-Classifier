def solve():
    """Index: 6360.
    Returns: the cost of a scoop of ice cream.
    """
    # L1
    meal_cost_per_person = 10 # meal worth $10
    number_of_people = 3 # Elisa and her two friends
    total_meal_cost = meal_cost_per_person * number_of_people

    # L2
    initial_money = 45 # $45 Elisa had
    remaining_money_after_meals = initial_money - total_meal_cost

    # L3
    cost_per_scoop = remaining_money_after_meals / number_of_people

    # FA
    answer = cost_per_scoop
    return answer