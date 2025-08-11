def solve():
    """Index: 2294.
    Returns: the total number of oranges in all three buckets.
    """
    # L1
    oranges_first = 22 # 22 oranges in the first bucket
    more_in_second = 17 # 17 more oranges in the second bucket
    oranges_second = oranges_first + more_in_second

    # L2
    fewer_in_third = 11 # 11 fewer oranges in the third bucket than in the second
    oranges_third = oranges_second - fewer_in_third

    # L3
    total_oranges = oranges_first + oranges_second + oranges_third

    # FA
    answer = total_oranges
    return answer