def solve():
    """Index: 2994.
    Returns: the total time Nadine spends cleaning her dog in minutes.
    """
    # L1
    shampoo_time_per = 15 # 15 minutes per shampoo
    num_shampoos = 3 # shampoos him three times
    total_shampoo_time = shampoo_time_per * num_shampoos

    # L2
    hosing_time = 10 # spends 10 minutes hosing him off
    total_cleaning_time = total_shampoo_time + hosing_time

    # FA
    answer = total_cleaning_time
    return answer