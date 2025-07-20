def solve():
    """Index: 7350.
    Returns: the amount of money Tonya spent on paintbrushes.
    """
    # L1
    canvases_cost = 40.00 # 4 canvases cost $40.00
    paint_cost_divisor = 2 # 1/2 that much
    paint_cost = canvases_cost / paint_cost_divisor

    # L2
    easel_cost = 15.00 # spent $15.00 on an easel
    total_other_purchases = canvases_cost + paint_cost + easel_cost

    # L3
    total_spent = 90.00 # Tonya spent $90.00 on art supplies
    paintbrushes_cost = total_spent - total_other_purchases

    # FA
    answer = paintbrushes_cost
    return answer