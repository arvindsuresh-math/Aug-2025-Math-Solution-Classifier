def solve():
    """Index: 7178.
    Returns: how much more expensive the first TV was by cost per square inch.
    """
    # L1
    first_tv_width = 24 # 24 inches wide
    first_tv_height = 16 # 16 inches tall
    first_tv_area = first_tv_width * first_tv_height

    # L2
    first_tv_cost = 672 # It cost $672
    first_tv_cost_per_sq_inch = first_tv_cost / first_tv_area

    # L3
    new_tv_area = 1536 # His new TV is 1,536 square inches.

    # L4
    new_tv_cost = 1152 # costs $1152
    new_tv_cost_per_sq_inch = new_tv_cost / new_tv_area

    # L5
    new_tv_cost_per_sq_inch_as_per_L5 = 0.75 # WK
    cost_difference = first_tv_cost_per_sq_inch - new_tv_cost_per_sq_inch_as_per_L5

    # FA
    answer = cost_difference
    return answer