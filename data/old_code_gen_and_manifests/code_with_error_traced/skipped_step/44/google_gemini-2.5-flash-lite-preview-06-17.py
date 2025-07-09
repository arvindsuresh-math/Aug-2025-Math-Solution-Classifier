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
    accommodation_cost = budget * accommodation_percentage # eval: 150.0 = 1000 * 0.15

    #: L2

    #: L3
    entertainment_cost = budget * entertainment_percentage # eval: 250.0 = 1000 * 0.25

    #: L4
    coursework_materials_cost = budget - (accommodation_cost + accommodation_percentage + entertainment_cost) # eval: 599.85 = 1000 - (150.0 + 0.15 + 250.0)

    #: FA
    answer = coursework_materials_cost
    return answer # eval: return 599.85
