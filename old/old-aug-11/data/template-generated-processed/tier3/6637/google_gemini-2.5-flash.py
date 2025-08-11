def solve():
    """Index: 6637.
    Returns: the total capacity of 40 such containers filled with water.
    """
    # L1
    eight_liters = 8 # eight liters
    percentage_capacity = 20 # 20% the capacity
    full_percentage = 100 # WK
    single_container_capacity = full_percentage / percentage_capacity * eight_liters

    # L2
    num_containers = 40 # 40 such containers
    total_capacity = num_containers * single_container_capacity

    # FA
    answer = total_capacity
    return answer