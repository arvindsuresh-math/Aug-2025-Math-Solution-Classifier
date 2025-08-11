def solve():
    """Index: 4806.
    Returns: the total minutes Melissa spends on the project.
    """
    # L1
    time_buckle_per_shoe = 5 # 5 minutes to replace the buckle
    time_heel_per_shoe = 10 # 10 minutes to even out the heel
    total_time_per_shoe = time_buckle_per_shoe + time_heel_per_shoe

    # L2
    num_shoes = 2 # 2 shoes
    total_project_time = total_time_per_shoe * num_shoes

    # FA
    answer = total_project_time
    return answer