def solve():
    """Index: 1670.
    Returns: the number of oranges in the basket.
    """
    # L1
    apples_ratio_part = 3 # 3 times as many apples as oranges
    oranges_ratio_part = 1 # 3 times as many apples as oranges
    group_size = apples_ratio_part + oranges_ratio_part

    # L2
    total_fruit = 40 # holding 40 fruit altogether
    number_of_groups = total_fruit / group_size

    # L3
    oranges_count = number_of_groups * oranges_ratio_part

    # FA
    answer = oranges_count
    return answer