def solve():
    """Index: 6174.
    Returns: the number of additional batches of cookies Gigi can make.
    """
    # L1
    num_batches_baked = 3 # 3 batches of cookies
    flour_per_batch = 2 # 2 cups of flour
    flour_used = num_batches_baked * flour_per_batch

    # L2
    initial_flour_in_bag = 20 # bag of flour contains 20 cups of flour
    flour_remaining = initial_flour_in_bag - flour_used

    # L3
    additional_batches = flour_remaining / flour_per_batch

    # FA
    answer = additional_batches
    return answer