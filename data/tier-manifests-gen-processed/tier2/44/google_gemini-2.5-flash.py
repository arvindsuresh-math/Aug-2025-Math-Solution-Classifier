def solve():
    """Index: 44.
    Returns: the amount of money James spends on coursework materials.
    """
    # L1
    budget = 1000 # budget of $1000 per semester
    accommodation_percent_num = 15 # 15% on accommodation
    percent_factor = 0.01 # WK
    accommodation_cost = accommodation_percent_num * percent_factor * budget

    # L2
    food_percent_num = 30 # 30% of his money on food
    food_cost = food_percent_num * percent_factor * budget

    # L3
    entertainment_percent_num = 25 # 25% on entertainment
    entertainment_cost = entertainment_percent_num * percent_factor * budget

    # L4
    coursework_materials_cost = budget - (accommodation_cost + food_cost + entertainment_cost)

    # FA
    answer = coursework_materials_cost
    return answer