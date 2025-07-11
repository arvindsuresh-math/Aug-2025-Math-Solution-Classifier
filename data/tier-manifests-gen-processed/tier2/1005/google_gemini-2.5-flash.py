def solve():
    """Index: 1005.
    Returns: the total money spent by the friends.
    """
    # L1
    original_price_tshirt = 20 # original price of the t-shirt was 20 dollars
    discount_factor = 0.5 # 50% off
    discounted_tshirt_price = original_price_tshirt * discount_factor

    # L2
    num_friends = 4 # All four friends
    total_spent = num_friends * discounted_tshirt_price

    # FA
    answer = total_spent
    return answer