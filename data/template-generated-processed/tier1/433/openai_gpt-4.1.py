def solve():
    """Index: 433.
    Returns: the total amount Michael earned from selling his paintings.
    """
    # L1
    num_large = 5 # sold 5 large paintings
    price_large = 100 # charges $100 for a large painting
    earned_large = num_large * price_large

    # L2
    num_small = 8 # sold 8 small paintings
    price_small = 80 # charges $80 for a small painting
    earned_small = num_small * price_small

    # L3
    total_earned = earned_large + earned_small

    # FA
    answer = total_earned
    return answer