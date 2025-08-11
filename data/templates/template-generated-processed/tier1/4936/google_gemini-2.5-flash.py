def solve():
    """Index: 4936.
    Returns: how much more water can be put into the 6-liter bucket.
    """
    # L1
    five_liter_bucket_capacity = 5 # holding either 3, 5, or 6 liters. She fills the 5-liter bucket
    three_liter_bucket_capacity = 3 # holding either 3, 5, or 6 liters. pours as much as she can into the 3-liter bucket
    remainder_after_pouring_into_3l = five_liter_bucket_capacity - three_liter_bucket_capacity

    # L2
    six_liter_bucket_capacity = 6 # holding either 3, 5, or 6 liters. pours the remainder into the 6-liter bucket
    additional_capacity_6l_bucket = six_liter_bucket_capacity - remainder_after_pouring_into_3l

    # FA
    answer = additional_capacity_6l_bucket
    return answer