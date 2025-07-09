def solve(
    budget: int = 1000,  # James has a budget of $1000 per semester
    food_percentage: float = 0.3,  # He spends 30% of his money on food
    accommodation_percentage: float = 0.15,  # 15% on accommodation
    entertainment_percentage: float = 0.25  # 25% on entertainment
):
    """Index: 44.
    Returns: the amount of money James spends on coursework materials."""

    #: L1
    accommodation_cost = accommodation_percentage * budget # eval: 150.0 = 0.15 * 1000

    #: L2
    food_cost = 310.0 # eval: 310.0 = 310.0

    #: L3
    entertainment_cost = entertainment_percentage * budget # eval: 250.0 = 0.25 * 1000

    #: L4
    coursework_materials_cost = budget - (accommodation_cost + food_cost + entertainment_cost) # eval: 290.0 = 1000 - (150.0 + 310.0 + 250.0)

    #: FA
    answer = coursework_materials_cost
    return answer # eval: return 290.0
