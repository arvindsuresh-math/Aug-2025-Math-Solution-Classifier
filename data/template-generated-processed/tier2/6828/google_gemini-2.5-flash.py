def solve():
    """Index: 6828.
    Returns: the total cost of pencils and pens.
    """
    # L1
    pencil_cost = 2.50 # A pencil costs $2.50
    num_pencils = 38 # 38 pencils
    cost_pencils = pencil_cost * num_pencils

    # L2
    pen_cost = 3.50 # a pen costs $3.50
    num_pens = 56 # 56 pens
    cost_pens = pen_cost * num_pens

    # L3
    total_cost = cost_pencils + cost_pens

    # FA
    answer = total_cost
    return answer