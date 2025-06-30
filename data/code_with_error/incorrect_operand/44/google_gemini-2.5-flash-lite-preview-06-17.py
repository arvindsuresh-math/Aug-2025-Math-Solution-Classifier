def solve(
    budget: int = 1000, # James has a budget of $1000 per semester
    food_percentage: float = 0.30, # He spends 30% of his money on food
    accommodation_percentage: float = 0.15, # 15% on accommodation
    entertainment_percentage: float = 0.25 # 25% on entertainment
):
    """Index: 44.
    Returns: the amount of money James spends on coursework materials.
    """

    #: L1
    accommodation_cost = budget * accommodation_percentage

    #: L2
    food_cost = budget * accommodation_cost

    #: L3
    entertainment_cost = budget * entertainment_percentage

    #: L4
    coursework_materials_cost = budget - (accommodation_cost + food_cost + entertainment_cost)

    #: FA
    answer = coursework_materials_cost
    return answer