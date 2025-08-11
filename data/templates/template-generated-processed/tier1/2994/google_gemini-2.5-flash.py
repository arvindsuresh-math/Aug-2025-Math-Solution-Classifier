def solve():
    """Index: 2994.
    Returns: the total time spent cleaning the dog.
    """
    # L1
    minutes_per_shampoo = 15 # 15 minutes per shampoo
    num_shampoos = 3 # shampoos him three times
    total_shampoo_time = minutes_per_shampoo * num_shampoos

    # L2
    hosing_time = 10 # 10 minutes hosing him off outside
    total_cleaning_time = total_shampoo_time + hosing_time

    # FA
    answer = total_cleaning_time
    return answer