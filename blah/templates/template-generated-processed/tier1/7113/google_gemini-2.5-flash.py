def solve():
    """Index: 7113.
    Returns: the total ounces in the second large bucket.
    """
    # L1
    total_in_bigger_bucket = 23 # The total in the bigger bucket is now 23 ounces.
    ten_ounce_bucket_val = 10 # the ten-ounce bucket
    identified_bucket_value = total_in_bigger_bucket - ten_ounce_bucket_val

    # L3
    remaining_bucket_1 = 11 # One contains 11 ounces
    remaining_bucket_2 = 12 # one contains 12 ounces
    remaining_bucket_3 = 16 # one contains 16 ounces
    second_large_bucket_content = remaining_bucket_1 + remaining_bucket_2 + remaining_bucket_3

    # FA
    answer = second_large_bucket_content
    return answer