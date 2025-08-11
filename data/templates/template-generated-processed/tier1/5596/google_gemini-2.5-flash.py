def solve():
    """Index: 5596.
    Returns: the total number of whales in the sea next year.
    """
    # L1
    whales_last_year = 4000 # number of whales in the sea last year was 4000
    double_factor = 2 # double what it was last year
    whales_this_year = double_factor * whales_last_year

    # L2
    predicted_increase = 800 # 800 more whales in the sea next year
    whales_next_year = whales_this_year + predicted_increase

    # FA
    answer = whales_next_year
    return answer