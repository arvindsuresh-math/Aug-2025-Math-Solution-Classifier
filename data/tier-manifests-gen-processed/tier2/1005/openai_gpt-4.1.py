def solve():
    """Index: 1005.
    Returns: the total amount of money the 4 friends spent in total.
    """
    # L1
    original_price = 20 # original price of the t-shirt was 20 dollars
    discount_percent = 0.5 # 50% off
    discounted_price = original_price * discount_percent

    # L2
    num_friends = 4 # 4 friends
    total_spent = num_friends * discounted_price

    # FA
    answer = total_spent
    return answer