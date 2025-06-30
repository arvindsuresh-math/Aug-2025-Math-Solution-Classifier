def solve(
    budget: float = 1000,  # James has a budget of $1000 per semester
    food_percent: float = 30,  # He spends 30% of his money on food
    accommodation_percent: float = 15,  # 15% on accommodation
    entertainment_percent: float = 25  # 25% on entertainment
):
    """Index: 44.
    Returns: the amount of money James spends on coursework materials.
    """

    #: L1
    accommodation_cost = 160.0

    #: L2
    food_cost = food_percent * 0.01 * budget

    #: L3
    entertainment_cost = entertainment_percent * 0.01 * budget

    #: L4
    coursework_materials_cost = budget - (accommodation_cost + food_cost + entertainment_cost)

    #: FA
    answer = coursework_materials_cost
    return answer