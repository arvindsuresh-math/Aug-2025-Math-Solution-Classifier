def solve(
        budget: int = 1000, # budget of $1000 per semester
        food_percentage: float = 0.30, # 30% of his money on food
        accommodation_percentage: float = 0.15, # 15% on accommodation
        entertainment_percentage: float = 0.25 # 25% on entertainment
    ):
    """Index: 44.
    Returns: the amount of money James spends on coursework materials.
    """

    #: L1

    #: L2
    food_cost = food_percentage * budget # eval: 300.0 = 0.3 * 1000

    #: L3
    entertainment_cost = entertainment_percentage * budget # eval: 250.0 = 0.25 * 1000

    #: L4
    coursework_materials_cost = budget - (entertainment_percentage + food_cost + entertainment_cost) # eval: 449.75 = 1000 - (0.25 + 300.0 + 250.0)

    #: FA
    answer = coursework_materials_cost
    return answer # eval: return 449.75
