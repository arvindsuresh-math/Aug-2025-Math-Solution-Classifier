def solve():
    """Index: 1831.
    Returns: the total amount of money paid for the stationery.
    """
    # L1
    num_boxes = 15 # 15 boxes
    pencils_per_box = 80 # 80 pencils
    total_pencils = num_boxes * pencils_per_box

    # L2
    cost_per_pencil = 4 # cost of a pencil was $4
    total_cost_pencils = cost_per_pencil * total_pencils

    # L3
    multiplier_for_twice = 2 # twice as many pens
    twice_pencils = multiplier_for_twice * total_pencils

    # L4
    pens_more_than_twice = 300 # 300 more than twice as many pens
    total_pens = twice_pencils + pens_more_than_twice

    # L5
    cost_per_pen = 5 # $5 each (for pens)
    total_cost_pens = total_pens * cost_per_pen

    # L6
    total_stationery_cost = total_cost_pens + total_cost_pencils

    # FA
    answer = total_stationery_cost
    return answer