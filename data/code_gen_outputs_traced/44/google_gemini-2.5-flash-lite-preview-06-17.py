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
    food_cost = budget * food_percentage # eval: 300.0 = 1000 * 0.3
    #: L3
    entertainment_cost = budget * entertainment_percentage # eval: 250.0 = 1000 * 0.25
    #: L4
    coursework_materials_cost = budget - (accommodation_cost + food_cost + entertainment_cost) # eval: 300.0 = 1000 - (150.0 + 300.0 + 250.0)
    answer = coursework_materials_cost # FINAL ANSWER # eval: 300.0 = 300.0 # FINAL ANSWER
    return answer # eval: return 300.0