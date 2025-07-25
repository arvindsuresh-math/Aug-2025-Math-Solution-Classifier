def solve():
    """Index: 7054.
    Returns: the number of baguettes left.
    """
    # L1
    num_batches_per_day = 3 # 3 batches of baguettes a day
    baguettes_per_batch = 48 # Each batch has 48 baguettes
    total_made_per_day = num_batches_per_day * baguettes_per_batch

    # L2
    sold_first_batch = 37 # sold 37
    sold_second_batch = 52 # sold 52
    sold_third_batch = 49 # sold 49
    total_sold = sold_first_batch + sold_second_batch + sold_third_batch

    # L3
    baguettes_left = total_made_per_day - total_sold

    # FA
    answer = baguettes_left
    return answer