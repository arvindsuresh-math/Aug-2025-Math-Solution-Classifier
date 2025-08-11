def solve():
    """Index: 1418.
    Returns: the amount of money Maria will earn on the painting if she sells it for $200.
    """
    # L1
    canvas_multiplier = 3 # three times more than the brushes
    brushes_cost = 20 # set of brushes for $20
    canvas_cost = canvas_multiplier * brushes_cost

    # L2
    paint_price_per_liter = 8 # paint costs $8 per liter
    paint_liters_needed = 5 # needs at least 5 liters
    paint_cost = paint_price_per_liter * paint_liters_needed

    # L3
    painting_sale_price = 200 # sell it for $200
    total_earnings = painting_sale_price - paint_cost - canvas_cost - brushes_cost

    # FA
    answer = total_earnings
    return answer