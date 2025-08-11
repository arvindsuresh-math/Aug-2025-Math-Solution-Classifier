def solve():
    """Index: 775.
    Returns: the total number of pieces of fruit in all 3 buckets.
    """
    # L1
    bucket_c = 9 # bucket C has 9 pieces of fruit
    b_more_than_c = 3 # bucket B has 3 more pieces of fruit than bucket C
    bucket_b = bucket_c + b_more_than_c

    # L2
    a_more_than_b = 4 # bucket A has 4 more pieces of fruit than bucket B
    bucket_a = bucket_b + a_more_than_b

    # L3
    total_fruit = bucket_c + bucket_b + bucket_a

    # FA
    answer = total_fruit
    return answer