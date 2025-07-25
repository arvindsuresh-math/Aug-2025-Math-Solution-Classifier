def solve():
    """Index: 1402.
    Returns: the total time to dig the graves.
    """
    # L1
    time_per_adult_grave = 3 # 3 hours to dig an adult grave
    num_adult_graves = 5 # 5 adult graves
    total_time_adult_graves = time_per_adult_grave * num_adult_graves

    # L2
    time_per_child_grave = 2 # 2 hours to dig a child's grave
    total_time = total_time_adult_graves + time_per_child_grave

    # FA
    answer = total_time
    return answer