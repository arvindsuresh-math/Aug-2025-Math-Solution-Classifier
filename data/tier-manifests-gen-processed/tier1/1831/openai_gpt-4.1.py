def solve():
    """Index: 1831.
    Returns: the total amount of money the store paid for the stationery.
    """
    # L1
    num_boxes = 15 # store ordered 15 boxes
    pencils_per_box = 80 # each having 80 pencils
    num_pencils = num_boxes * pencils_per_box

    # L2
    cost_per_pencil = 4 # cost of a pencil was $4
    total_pencil_cost = cost_per_pencil * num_pencils

    # L3
    pens_multiplier = 2 # twice as many pens as pencils
    twice_pencils = pens_multiplier * num_pencils

    # L4
    pens_extra = 300 # 300 more than twice as many pens
    num_pens = twice_pencils + pens_extra

    # L5
    cost_per_pen = 5 # cost of the pens was $5
    total_pen_cost = num_pens * cost_per_pen

    # L6
    total_cost = total_pen_cost + total_pencil_cost

    # FA
    answer = total_cost
    return answer