def solve():
    """Index: 6806.
    Returns: the number of Russian dolls Daniel can buy at the discounted price.
    """
    # L1
    original_doll_price = 4 # normally cost $4 each
    dolls_he_can_buy = 15 # buy 15 Russian dolls
    total_savings = dolls_he_can_buy * original_doll_price

    # L2
    discounted_doll_price = 3 # price suddenly drops to $3 each
    dolls_can_buy_now = total_savings / discounted_doll_price

    # FA
    answer = dolls_can_buy_now
    return answer