def solve():
    """Index: 1418.
    Returns: the net earnings Maria will make on the painting.
    """
    # L1
    brushes_cost = 20 # a set of brushes for $20
    canvas_multiplier = 3 # three times more than the brushes
    canvas_cost = canvas_multiplier * brushes_cost

    # L2
    paint_cost_per_liter = 8 # $8 per liter
    paint_liters_needed = 5 # needs at least 5 liters
    paint_cost = paint_cost_per_liter * paint_liters_needed

    # L3
    selling_price = 200 # sell it for $200
    net_earnings = selling_price - paint_cost - canvas_cost - brushes_cost

    # FA
    answer = net_earnings
    return answer