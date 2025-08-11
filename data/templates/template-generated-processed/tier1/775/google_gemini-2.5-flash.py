def solve():
    """Index: 775.
    Returns: the total number of pieces of fruit in all 3 buckets.
    """
    # L1
    c_fruits = 9 # If bucket C has 9 pieces of fruit
    b_more_than_c = 3 # bucket B has 3 more pieces of fruit than bucket C
    b_fruits = c_fruits + b_more_than_c

    # L2
    a_more_than_b = 4 # Bucket A has 4 more pieces of fruit than bucket B
    a_fruits = b_fruits + a_more_than_b

    # L3
    total_fruits = c_fruits + b_fruits + a_fruits

    # FA
    answer = total_fruits
    return answer