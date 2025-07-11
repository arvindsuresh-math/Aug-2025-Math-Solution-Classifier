def solve():
    """Index: 1402.
    Returns: the total time Dan spends digging 5 adult graves and one child's grave.
    """
    # L1
    hours_per_adult_grave = 3 # it takes Dan 3 hours to dig an adult grave
    num_adult_graves = 5 # 5 adult graves
    total_adult_time = hours_per_adult_grave * num_adult_graves

    # L2
    hours_per_child_grave = 2 # 2 hours to dig a child's grave
    total_time = total_adult_time + hours_per_child_grave

    # FA
    answer = total_time
    return answer