def solve():
    """Index: 2294.
    Returns: the total number of oranges in all the buckets.
    """
    # L1
    first_bucket_oranges = 22 # 22 oranges in the first bucket
    more_in_second_bucket = 17 # 17 more oranges in the second bucket
    second_bucket_oranges = first_bucket_oranges + more_in_second_bucket

    # L2
    fewer_in_third_bucket = 11 # 11 fewer oranges in the third bucket
    third_bucket_oranges = second_bucket_oranges - fewer_in_third_bucket

    # L3
    total_oranges = first_bucket_oranges + second_bucket_oranges + third_bucket_oranges

    # FA
    answer = total_oranges
    return answer