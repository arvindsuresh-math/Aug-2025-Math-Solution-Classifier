def solve():
    """Index: 923.
    Returns: the total cost of the quilt.
    """
    # L1
    length = 7 # 7 foot
    width = 8 # 8-foot
    area = length * width

    # L2
    cost_per_sq_foot = 40 # $40 per square foot
    total_cost = cost_per_sq_foot * area

    # FA
    answer = total_cost
    return answer