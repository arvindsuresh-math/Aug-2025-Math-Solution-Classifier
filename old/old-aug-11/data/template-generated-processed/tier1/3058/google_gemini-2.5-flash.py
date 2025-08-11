def solve():
    """Index: 3058.
    Returns: the number of bones Barkley has buried.
    """
    # L1
    bones_per_month = 10 # 10 new dog bones
    num_months = 5 # After 5 months
    total_bones_received = bones_per_month * num_months

    # L2
    bones_available = 8 # has 8 bones available
    bones_buried = total_bones_received - bones_available

    # FA
    answer = bones_buried
    return answer