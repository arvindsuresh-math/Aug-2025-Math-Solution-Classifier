def solve():
    """Index: 6060.
    Returns: the amount more money Colleen paid than Joy for her pencils.
    """
    # L1
    colleen_pencils = 50 # Colleen has 50 pencils
    joy_pencils = 30 # Joy has 30 pencils
    pencils_difference = colleen_pencils - joy_pencils

    # L2
    cost_per_pencil = 4 # $4 each
    extra_cost = cost_per_pencil * pencils_difference

    # FA
    answer = extra_cost
    return answer