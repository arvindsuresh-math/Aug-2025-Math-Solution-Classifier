def solve():
    """Index: 44.
    Returns: the amount James spends on coursework materials.
    """
    # L1
    accommodation_percent = 15 # 15% on accommodation
    percent_factor = 0.01 # WK
    budget = 1000 # budget of $1000 per semester
    accommodation_spent = accommodation_percent * percent_factor * budget

    # L2
    food_percent = 30 # 30% on food
    food_spent = food_percent * percent_factor * budget

    # L3
    entertainment_percent = 25 # 25% on entertainment
    entertainment_spent = entertainment_percent * percent_factor * budget

    # L4
    coursework_spent = budget - (accommodation_spent + food_spent + entertainment_spent)

    # FA
    answer = coursework_spent
    return answer